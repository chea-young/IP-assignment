# Coding 시험 요령
주어진 문제들을 한정된 시간내에 풀도록 한다. 시간이 모자랄 수 있고, 부분적으로 틀린 solution을 제출할 수도 있으며, 시간이 모자라 못 풀 수도 있다.

여러분이 제출하는 결과들은 다음 측면에서 평가될 것이다.
- 얼마나 정확한 solution을 제공하느냐?
- 주어진 시간내에 얼마나 많은 문제를 푸느냐?
- Input 크기가 클 때, performance가 좋은가?
- 기타 부가점: coding style, 가독성, compactness 등

## (문제 예시) q0. Vowel Count
Return the number (count) of vowels in the given string.

We will consider `a`, `e`, `i`, `o`, `u` as vowels.

The input string will only consist of lower case letters and/or spaces.

## Coding and Testing
Starter code가 test function과 함께 문제 번호로 시작되는 file에 주어져 있다: `q0_test.py`. 여기에 code를 삽입하고, test가 통과할 때까지 수정한다. (시간 없으면 pass)

To test your code in this file,
```bash
$ pytest q0_test.py
```

To test all files with starting or ending with 'test' name in the current directory :
```bash
$ pytest
```

> 참고: pytest를 실행할 때는 stdout, stderr로 output이 print되지 않는다. 

Test function 실행시키지 않고 직접 Python Interpreter로 실행시키려면, 파일의 끝에 다음과 같이 coding한 function(또는 class)를 부르는 code를 삽입하라.

```Python
if __name__ == '__main__':
    get_count("abracadabra")
```

> 이렇게 해도 pytest 실행에 영향이 없다. 이 script 파일은 pytest에서 main으로 실행되지 않고 module로 import되기 때문.

## Local Repository 이용하여 문제를 푼다.
문제를 푸는 과정에 여러분이 clone한 local repository에서 새로운 commit들을 만들 수 있다. (물론, 원본이 있는 jinpyohong's repository에 push는 허용되지 않는다.)

## 답안 제출
변경사항을 모두 commit한다. 그리고, git repository 포함하는 폴더 전체(여기서는 exam directory)을 zip으로 압축한 exam.zip 파일을 eclass에 upload한다.
다시 말해, local repository와 working copy 모두를 제출하는 것이다.

## 배점
- q1, q2, q3: 각 10점
- q4, q5, q6: 각 15점
- clients.py: 25점
