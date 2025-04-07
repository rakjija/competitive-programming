print(len(input().split()))

"""
split() 메서드의 sep 인자의 기본값은 None임
None은 모든 whitespace(스페이스, 탭, 줄바꿈 등)를 기준으로 나눔
그리고, 문자열 앞뒤 공백은 자동으로 무시됨

한번 실패했는데
이렇게 작성했음
print(len(input().strip().split(' ')))

이게 틀린 이유는.. 
strip()은 공백만 제거할 뿐 \t, \n 과 같은 것들은 제거하지 못하기 때문임
그리고 split()을 통해서도 제거하지 못함
"""
