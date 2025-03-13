from enum import Enum


class CartStatusEnum(Enum):
    forming = 'forming'
    waiting_for_accept = 'waiting for accept'
    accepted = 'accepted'
