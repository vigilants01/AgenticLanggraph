from pydantic import BaseModel
from typing import Literal

class portfoliostate(BaseModel):
    amount_usd: float
    total_usd: float =0
    target_currency: Literal['INR','EUR']
    total_inr: float=0
    total_eur: float=0

def cal_total(state: portfoliostate):
    state.total_usd = state.amount_usd * 1.5
    return state

def cal_total_inr(state: portfoliostate):
    state.total_inr = state.total_usd * 80
    return state

def cal_total_eur(state: portfoliostate):
    state.total_eur = state.total_usd * 0.9
    return state

def choose_conversion(state: portfoliostate) -> str:
    return state.target_currency