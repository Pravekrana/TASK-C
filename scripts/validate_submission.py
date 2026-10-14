"""Local evidence and layout checks; no network or client system access."""
from pathlib import Path
import hashlib
import json
import math
import re
from pypdf import PdfReader
import pdfplumber
from financial_model import calculate

ROOT=Path(__file__).resolve().parents[1]


def main():
    required=['README.md','SUBMISSION_INSTRUCTIONS.md','QUALITY_CHECK.md','.gitignore',
      'submission/case-study.md','submission/case-study.pdf','submission/client-note.md','submission/client-note.pdf',
      'submission/submission-form.md','submission/form-answers-copy-paste.md','submission/prototype-results.md',
      'appendix/technical-architecture.md','appendix/data-contracts.md','appendix/assumptions-and-evidence.md',
      'appendix/evaluation-protocol.md','appendix/financial-model.md','appendix/financial-model.json',
      'prototype/README.md','prototype/requirements.txt','prototype/run_demo.py',
      'prototype/src/models.py','prototype/src/validation.py','prototype/src/baseline.py',
      'prototype/src/optimizer.py','prototype/src/metrics.py','prototype/src/reporting.py',
      'prototype/data/synthetic_stock.csv','prototype/data/synthetic_demand.csv','prototype/data/synthetic_offcuts.csv',
      'prototype/tests/test_validation.py','prototype/tests/test_optimizer.py','prototype/tests/test_metrics.py',
      'scripts/build_pdfs.py','scripts/validate_submission.py','scripts/financial_model.py']
    for p in required:
        assert (ROOT/p).is_file() and (ROOT/p).stat().st_size, f'Missing/empty {p}'
    hashes=json.loads((ROOT/'scripts/source-checksums.json').read_text())
    for f,h in hashes.items():
        assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h, f'Source changed: {f}'
    pdfs={}
    for name,expected in [('case-study',6),('client-note',1)]:
        p=ROOT/'submission'/f'{name}.pdf'
        reader=PdfReader(p)
        assert len(reader.pages)==expected,(name,len(reader.pages))
        texts=[page.extract_text() for page in reader.pages]
        assert all('CONFIDENTIAL' in t for t in texts)
        normalise=lambda s: re.sub('[^a-z0-9]', '', s.lower())
        pdf_text=normalise(' '.join(texts))
        for line in (ROOT/'submission'/f'{name}.md').read_text(encoding='utf-8').splitlines():
            if not line.strip() or 'PAGEBREAK' in line:
                continue
            for piece in (line.split('|') if line.startswith('|') else [line]):
                token=normalise(piece)
                assert not token or token in pdf_text, f'Missing PDF text: {name}: {piece[:80]}'
        assert all(len(t)>300 for t in texts)
        assert not any('\ufffd' in t or '\u25a0' in t for t in texts)
        with pdfplumber.open(p) as doc:
            bounds=[]
            for page in doc.pages:
                chars=page.chars
                assert chars
                bad=[c for c in chars if c['x0']<38 or c['x1']>page.width-30 or c['top']<20 or c['bottom']>page.height-18]
                assert not bad, f'Text outside safe bounds: {name} page {page.page_number}'
                body=[c for c in chars if c['top']<page.height-50]
                assert min(c['size'] for c in body)>=8.3-0.01
                bounds.append(dict(page=page.page_number,left=min(c['x0'] for c in chars),right=max(c['x1'] for c in chars),top=min(c['top'] for c in chars),bottom=max(c['bottom'] for c in chars)))
        pdfs[name]=dict(pages=expected,text_bounds=bounds)
    text=' '.join(p.extract_text() for p in PdfReader(ROOT/'submission/case-study.pdf').pages)
    for anchor in ['Executive decision','Operating model','People and the decision','Exactly five','Options and conditional','Read-only by design','paired evaluation','Value, cost','Six weeks','Risk register']:
        assert anchor in text, f'Missing case section: {anchor}'
    source=(ROOT/'Task 3 V2.txt').read_text(encoding='utf-8').splitlines()
    prefixes=('In two sentences:','Who are the people','The five questions','Which options','How will the client','What does this cost','Timeline.','Where did you push','What is most likely','What did you use AI','Github Repo URL')
    qs=[line for line in source if line.startswith(prefixes)]
    assert len(qs)==11
    form=(ROOT/'submission/submission-form.md').read_text(encoding='utf-8')
    copy=(ROOT/'submission/form-answers-copy-paste.md').read_text(encoding='utf-8')
    positions=[form.index('## '+str(i)+'. '+q) for i,q in enumerate(qs,1)]
    assert positions==sorted(positions)
    for i,q in enumerate(qs,1):
        h='## '+str(i)+'. '+q
        start=form.index(h)+len(h)
        end=positions[i] if i<11 else len(form)
        answer=form[start:end].strip()
        assert len(answer)>100
        cp=copy.split(f'<!-- START ANSWER {i} -->')[1].split(f'<!-- END ANSWER {i} -->')[0].strip()
        assert answer==cp,f'Form copy mismatch {i}'
    f=calculate(); stored=json.loads((ROOT/'appendix/financial-model.json').read_text())
    assert f==stored
    expected={'labour':26400,'internal_delivery_cost':31050,'delivery_margin':.31,'first_year_vendor_spend':51000,'base_total_outlay':61000}
    for k,v in expected.items(): assert math.isclose(f[k],v)
    b=f['scenarios']['base']
    for k,v in {'gross_value':160000,'recovered_equivalent_t':320,'full_operating_year_net':99000,'operating_payback_months':3.75,'first_year_break_even_pp':.305,'kickoff_year_net':80538.46153846153}.items():
        assert math.isclose(b[k],v)
    assert f['stage01_internal']+f['stage2_internal']==f['internal_delivery_cost']
    assert 7500+7500+15000+10000+5000==f['client_fee']
    result=dict(status='PASS',required_files=len(required),source_hashes_unchanged=True,pdf_checks=pdfs,form_fields=11,form_copy_consistent=True,financial_arithmetic='PASS',pdf_text_retention='PASS')
    (ROOT/'scripts/validation-results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
