"""Render the authored Markdown with explicit page breaks; no content shrinking."""
from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Flowable
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4

ROOT = Path(__file__).resolve().parents[1]
NAVY = colors.HexColor('#17324d')
TEAL = colors.HexColor('#137d8c')
BODY = colors.HexColor('#263746')
STYLES = {
 'body': ParagraphStyle('body', fontName='Helvetica', fontSize=9.5, leading=12.1, textColor=BODY, spaceAfter=6),
 'h1': ParagraphStyle('h1', fontName='Helvetica-Bold', fontSize=19, leading=22, textColor=NAVY, spaceAfter=10),
 'h2': ParagraphStyle('h2', fontName='Helvetica-Bold', fontSize=11.3, leading=14, textColor=TEAL, spaceBefore=4, spaceAfter=6),
 'cell': ParagraphStyle('cell', fontName='Helvetica', fontSize=8.6, leading=10.5, textColor=BODY),
 'th': ParagraphStyle('th', fontName='Helvetica-Bold', fontSize=8.5, leading=10.5, textColor=colors.white),
}

def inline(s):
    s = escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = s.replace(' -> ', ' &gt; ')
    return s

class Workflow(Flowable):
    def __init__(self):
        super().__init__(); self.width=499; self.height=66
    def draw(self):
        labels=['Read-only exports','Validate + reconcile','Eligibility + compare',
                'Human approval','Existing workflow','Actuals + value']
        for i,label in enumerate(labels):
            row,col=divmod(i,3); x=col*168; y=36-row*33
            self.canv.setFillColor(colors.HexColor('#edf5f6'))
            self.canv.setStrokeColor(TEAL)
            self.canv.roundRect(x,y,157,26,4,fill=1,stroke=1)
            self.canv.setFillColor(NAVY); self.canv.setFont('Helvetica-Bold',8.3)
            self.canv.drawCentredString(x+78.5,y+10,label)
            if col<2:
                self.canv.drawString(x+159,y+10,'>')
        self.canv.setStrokeColor(TEAL)
        self.canv.line(493,36,493,32); self.canv.line(493,32,3,32); self.canv.line(3,32,3,29)


def parse(text, note=False):
    story=[]; lines=text.splitlines(); i=0
    while i<len(lines):
        line=lines[i].strip()
        if not line: i+=1; continue
        if line=='<!-- PAGEBREAK -->': story.append(PageBreak()); i+=1; continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                cells=[c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'[-: ]+',c) for c in cells): rows.append(cells)
                i+=1
            n=len(rows[0]); widths={3:[124,183,200],4:[110,145,152,100],5:[107,93,105,101,101],6:[94,86,87,81,77,82]}[n]
            data=[[Paragraph(inline(c),STYLES['th' if r==0 else 'cell']) for c in row] for r,row in enumerate(rows)]
            table=Table(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
            table.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),NAVY),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#f1f5f8'),colors.white]),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),('LINEBELOW',(0,-1),(-1,-1),.4,colors.HexColor('#bacbd5'))]))
            story.extend([table,Spacer(1,7)]); continue
        if line.startswith('# '): style='h1'; line=line[2:]
        elif line.startswith('## '): style='h2'; line=line[3:]
        else: style='body'
        story.append(Paragraph(inline(line),STYLES[style]))
        if line=='6 | Read-only by design; people retain control': story.append(Workflow())
        i+=1
    return story


def footer(canvas,doc):
    w,h=A4
    canvas.setStrokeColor(colors.HexColor('#c4d1da')); canvas.line(44,39,w-44,39)
    canvas.setFont('Helvetica',7.5); canvas.setFillColor(NAVY)
    canvas.drawString(44,27,'CONFIDENTIAL | Client B | Assessment proposal - illustrative economics')
    canvas.drawRightString(w-44,27,str(doc.page))


def build(name):
    out=ROOT/'submission'/f'{name}.pdf'
    STYLES['body'].fontSize = 10.2 if name == 'client-note' else 9.5
    STYLES['body'].leading = 13.3 if name == 'client-note' else 12.1
    doc=SimpleDocTemplate(str(out),pagesize=A4,rightMargin=44,leftMargin=44,topMargin=35,bottomMargin=48,
                         title='Client B | '+name.replace('-',' ').title(),author='FDE case study submission')
    doc.build(parse((ROOT/'submission'/f'{name}.md').read_text(encoding='utf-8')),onFirstPage=footer,onLaterPages=footer)
    print(out)

if __name__=='__main__':
    build('case-study'); build('client-note')
