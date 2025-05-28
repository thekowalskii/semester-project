from enum import Enum


class OrderStatusEnum(Enum):
    forming = 'forming'
    waiting_for_accept = 'waiting for accept'
    accepted = 'accepted'
