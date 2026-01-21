# [Silver III] 파일 정리 - 20291 

[문제 링크](https://www.acmicpc.net/problem/20291) 

### 성능 요약

메모리: 53452 KB, 시간: 1432 ms

### 분류

자료 구조, 문자열, 정렬, 집합과 맵, 해시를 사용한 집합과 맵, 트리를 사용한 집합과 맵, 파싱

### 제출 일자

2026년 1월 21일 03:30:55

### 문제 설명

<p>친구로부터 노트북을 중고로 산 스브러스는 노트북을 켜자마자 경악할 수밖에 없었다. 바탕화면에 온갖 파일들이 정리도 안 된 채 가득했기 때문이다. 그리고 화면의 구석에서 친구의 메시지를 확인할 수 있었다.</p>

<p style="background: rgb(238, 238, 238); border: 1px solid rgb(204, 204, 204); padding: 5px 10px;">바탕화면의 파일들에는 값진 보물에 대한 정보가 들어 있어. 하나라도 지우게 된다면 보물은 물론이고 다시는 노트북을 쓸 수 없게 될 거야. 파일들을 잘 분석해서 보물의 주인공이 될 수 있길 바랄게. 힌트는 “확장자”야.</p>

<p>화가 났던 스브러스는 보물 이야기에 금세 화가 풀렸고 보물의 정보를 알아내려고 애썼다. 하지만 파일이 너무 많은 탓에 이내 포기했고 보물의 절반을 보상으로 파일의 정리를 요청해왔다. 스브러스의 요청은 다음과 같다.</p>

<ul>
	<li>파일을 확장자 별로 정리해서 몇 개씩 있는지 알려줘</li>
	<li>보기 편하게 확장자들을 사전 순으로 정렬해 줘</li>
</ul>

<p>그럼 보물의 절반을 얻어내기 위해 얼른 스브러스의 노트북 파일 정리를 해줄 프로그램을 만들자!</p>

### 입력 

 <p>첫째 줄에 바탕화면에 있는 파일의 개수 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>이 주어진다. (<mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c></mjx-mn><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mi class="mjx-i" space="4"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi><mjx-mo class="mjx-n" space="4"><mjx-c class="mjx-c2264"></mjx-c></mjx-mo><mjx-mn class="mjx-n" space="4"><mjx-c class="mjx-c35"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn><mjx-mtext class="mjx-n"><mjx-c class="mjx-cA0"></mjx-c></mjx-mtext><mjx-mn class="mjx-n"><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>1</mn><mo>≤</mo><mi>N</mi><mo>≤</mo><mn>50</mn><mtext> </mtext><mn>000</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$1 \leq N \leq 50\ 000$</span></mjx-container>)</p>

<p>둘째 줄부터 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mi class="mjx-i"><mjx-c class="mjx-c1D441 TEX-I"></mjx-c></mjx-mi></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mi>N</mi></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$N$</span></mjx-container>개 줄에 바탕화면에 있는 파일의 이름이 주어진다. 파일의 이름은 알파벳 소문자와 점(<span style="color:#e74c3c;"><code>.</code></span>)으로만 구성되어 있다. 점은 정확히 한 번 등장하며, 파일 이름의 첫 글자 또는 마지막 글자로 오지 않는다. 각 파일의 이름의 길이는 최소 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c33"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>3</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$3$</span></mjx-container>, 최대 <mjx-container class="MathJax" jax="CHTML" style="font-size: 109%; position: relative;"><mjx-math class="MJX-TEX" aria-hidden="true"><mjx-mn class="mjx-n"><mjx-c class="mjx-c31"></mjx-c><mjx-c class="mjx-c30"></mjx-c><mjx-c class="mjx-c30"></mjx-c></mjx-mn></mjx-math><mjx-assistive-mml unselectable="on" display="inline"><math xmlns="http://www.w3.org/1998/Math/MathML"><mn>100</mn></math></mjx-assistive-mml><span aria-hidden="true" class="no-mathjax mjx-copytext">$100$</span></mjx-container>이다.</p>

### 출력 

 <p>확장자의 이름과 그 확장자 파일의 개수를 한 줄에 하나씩 출력한다. 확장자가 여러 개 있는 경우 확장자 이름의 사전순으로 출력한다.</p>


## 문제 해결 아이디어

확장자별로 몇개 있는지 센 후에, 해당 확장자들을 사전순으로 + 개수를 함께 출력한다.   

형식이 `파일명.확장자`로 고정되어 있기 때문에 정규식과 group을 사용하여 `확장자`를 분리해주려 했다.    

`tmp = p.search(f)`로 input에서 형식(`[a-z]*.([a-z]*)`)에 맞는 부분을 `tmp.group(1)` 그룹화하였고, 딕셔너리를 통해 그룹화한 확장자를 key로 하여 개수를 세주었다. 그리고 key를 기준으로 정렬하였다.     


**`re.compile(...)`의 시간복잡도** p = re.compile(r'[a-z]*.([a-z]*)')   

패턴 길이에 비례하는 작업으로, 상수 길이이다. ⇒ O([paturn])   

이 문제와 같이 패턴 길이가 고정이면 O(1)   


**`p.search(f)`의 시간복잡도**   

이 패턴은 단순하여 O(m) 정도의 시간 복잡도를 가진다. (m = 문자열 길이)   

그러나 복잡한 패턴(`*`가 겹치고 애매하면 백트래킹 가능성)에선 최악의 경우 O(m^2)도 가능하다.   

| 코드 | 시간복잡도 |
| --- | --- |
| `re.compile(...)` | **O(1)** (패턴 길이 상수) |
| `p.search(f)` (평균) | **O(m)** |
| `p.search(f)` (이론적 최악) | **O(m²)** |
| 전체 루프 (`n`개 파일) | **O(n · m)** |

위와 같은 방식으로 맞추었고, 정답 코드는 최종 코드와 같다.   

## Input 반례 (해결 과정)

반례는 아니지만, 정규식이 아니라 `split`을 사용하면 더 간단하게 풀 수도 있다.    

`ext = f.split('.')[-1]`방식은 O(m)으로 실행되어 백트래킹 위험도 낮고 가독성이 더 좋다고 할 수 있다.    

## 최종 코드

```python
import re
n = int(input())
file_ = []
for i in range(n):
    file_.append(input())

p = re.compile(r'[a-z]*.([a-z]*)')
result = {}

for f in file_:
    tmp = p.search(f)
    if tmp.group(1) not in result:
        result[tmp.group(1)] = 1
    else:
        result[tmp.group(1)] += 1

for k, v in sorted(result.items()):
    print(k, v)
```
