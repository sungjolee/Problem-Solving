def solution(n, k):
    service = n // 10
    k -= service
    return n * 12000 + k * 2000