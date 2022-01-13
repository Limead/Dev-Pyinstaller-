# Dev-Pyinstaller-

# pyinstaller + pyqt5 를 통한 툴 개발

AI와 관련된 부분은 아니지만 개발자로써 유용한 패키지가 있어 사용법 및 테스트로 만들어본 결과물을 공유합니다. 사용에 능숙해지면 AI관련 툴 제작도 가능하지 않을까...? 싶습니다.

# 📃 pyinstaller

---

pyinstaller는 py 스크립트 파일을 exe 실행 파일로 변환해주는 패키지입니다. 

해당 패키지 기능을 이용해 간단하게 실행시킬수 있는 exe 형태로 툴을 제작할 수 있습니다.

### # pyinstaller 설치

pyinstaller는 pip 를 사용해서 쉽게 설치 할 수 있습니다.

```
pip install pyinstaller
```

최신 버전으로 업그레이드는 --upgrade 옵션을 사용합니다.

```
pip install --upgrade pyinstaller
```

다음과 같이 pyinstaller 를 설치할 수 있습니다.

![https://blog.kakaocdn.net/dn/mrJBn/btqNQv5m6rB/IAbM1XCi6R3y2pfe3Aig1K/img.png](https://blog.kakaocdn.net/dn/mrJBn/btqNQv5m6rB/IAbM1XCi6R3y2pfe3Aig1K/img.png)

pyinstaller 설치 화면

### # pyinstaller 옵션

패키징 : 설치 완료 후 패키징을 할 파이썬 코드를 인자값으로 넘기면 됩니다.

```
pyinstaller sample.py
```

단일파일 : 디렉토리 형태로 바이너리를 만들기 때문에 단일 파일로 패키징 하기 위해서는 --onefile 옵션을 사용합니다.

```
pyinstaller --onefile sample.py
```

콘솔창(cmd.exe) 없애기 : Console 창을 열지 않고 구동 시킵니다.

```
pyinstaller --noconsole --onefile sample.py
```

아이콘 사용 : 본인이 제작한 .ico 파일로 아이콘 이미지 변경 시킬 수 있습니다.

```
pyinstaller --noconsole --icon=icon.ico --onefile sample.py
```

자세한 옵션은 -h 옵션을 통해 확인 할 수 있습니다.

![https://blog.kakaocdn.net/dn/K8wCW/btqNLQDY4kW/ct7fTcmSdKwgFakgPkdU2k/img.png](https://blog.kakaocdn.net/dn/K8wCW/btqNLQDY4kW/ct7fTcmSdKwgFakgPkdU2k/img.png)

# 📃 PyQt5

---

## **PyQt5에 대해**

![https://wikidocs.net/images/page/21849/0_pyqt_logo.png](https://wikidocs.net/images/page/21849/0_pyqt_logo.png)

- PyQt5는 Qt5 어플리케이션 프레임워크에 대한 파이썬 버전입니다. Qt는 플랫폼에 관계없이 다양한 기능을 포함하는 C++ 라이브러리이자 개발툴입니다.
- PyQt5는 이러한 1000여 개의 클래스들을 포함하는 파이썬 모듈의 모음입니다.
- PyQt5는 윈도우, 리눅스, macOS, 안드로이드, iOS를 지원합니다.
- PyQt5의 홈페이지([https://www.riverbankcomputing.com/software/pyqt/intro](https://www.riverbankcomputing.com/software/pyqt/intro))에서 최신의 그리고 안정적인 버전의 PyQt5와 최신 버전의 문서를 얻을 수 있습니다.
- PyQt5 개발자는 GPL과 상업용 라이센스 중 하나를 선택할 수 있습니다.(PyQt5 라이센스 관련: [https://www.riverbankcomputing.com/commercial/license-faq](https://www.riverbankcomputing.com/commercial/license-faq))

PyQt5 모듈을 이용하여 원하는 Gui 형태로 툴을 개발 할 수 있습니다.

아래 PyQt5 튜토리얼을 통해 사용법을 익힐 수 있습니다.

[https://wikidocs.net/book/2165](https://wikidocs.net/book/2165)

# 📃 활용

---

스크립트를 작성한 뒤 pyinstaller를 이용해 간단하게 점심을 랜덤으로 3개까지 추천해주는 프로그램(exe파일)을 개발하였습니다.\
![image](https://user-images.githubusercontent.com/97657857/149314850-a591d287-c571-45a4-8af9-5fbcaedd253b.png)


# 🌈 Reference

---

출처:

- pyinstaller 사용법

[https://greensul.tistory.com/76](https://greensul.tistory.com/76)

[초록술]

- Pyqt5 사용법

[https://wikidocs.net/21849](https://wikidocs.net/21849)

---

**E.o.D.**
