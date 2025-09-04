def add_numbers(a, b):
    """
    두 수를 받아서 그 합을 반환하는 함수
    
    Args:
        a (float): 첫 번째 수
        b (float): 두 번째 수
    
    Returns:
        float: 두 수의 합
    """
    return a + b

# 테스트 코드
if __name__ == "__main__":
    result = add_numbers(3, 5)
    print(f"3 + 5 = {result}")
    
    result2 = add_numbers(10.5, 2.3)
    print(f"10.5 + 2.3 = {result2}")