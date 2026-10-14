"""Executable hypothetical model. All amounts USD; improvements are fractions."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]

def calculate():
    labour=15*800+12*700+5*600+3*1000
    infrastructure=600
    contingency=(labour+infrastructure)*.15
    internal=labour+infrastructure+contingency
    fee=45000
    support=500*12
    cases={}
    for name,tonnes,eligible,improvement,value,friction in [
        ('downside',50000,.3,.002,350,15000),
        ('base',80000,.5,.008,500,10000),
        ('upside',80000,.7,.012,600,15000)]:
        scope=tonnes*eligible
        recovered=scope*improvement
        gross=recovered*value
        recurring_net=gross-support-friction
        cases[name]=dict(annual_input_t=tonnes,eligible_share=eligible,eligible_t=scope,
            improvement_fraction=improvement,improvement_pp=improvement*100,net_value_per_t=value,
            recovered_equivalent_t=recovered,gross_value=gross,friction=friction,
            annual_net_after_recurring=recurring_net,full_operating_year_net=recurring_net-fee,
            kickoff_year_net=gross*46/52-support-friction-fee,
            operating_payback_months=fee/(recurring_net/12) if recurring_net>0 else None,
            first_year_break_even_pp=(fee+support+friction)/(scope*value)*100)
    sensitivity=[]
    for scope in [15000,40000,56000]:
        for delta in [.002,.005,.008,.012]:
            gross=scope*delta*500
            sensitivity.append(dict(eligible_t=scope,improvement_pp=delta*100,gross=gross,net_full_year=gross-61000))
    return dict(currency='USD, hypothetical only',labour=labour,infrastructure=infrastructure,
        contingency=contingency,internal_delivery_cost=internal,client_fee=fee,
        delivery_contribution=fee-internal,delivery_margin=(fee-internal)/fee,
        stage01_internal=(5*800+4*700+1*600+1*1000+600)*1.15,
        stage2_internal=(10*800+8*700+4*600+2*1000)*1.15,
        annual_support=support,provider_annual_support_cost=300*12,
        first_year_vendor_spend=fee+support,base_total_outlay=fee+support+10000,
        base_kickoff_payback_months=6/52*12+cases['base']['operating_payback_months'],
        recurring_break_even_pp=(support+10000)/(40000*500)*100,
        kickoff_break_even_pp=(fee+support+10000)/(40000*500*(46/52))*100,
        scenarios=cases,sensitivity=sensitivity)

if __name__=='__main__':
    result=calculate()
    path=ROOT/'appendix/financial-model.json'
    path.write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps(result,indent=2))
