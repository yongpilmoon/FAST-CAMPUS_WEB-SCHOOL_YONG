# 개발 환경 세팅하기

#### 기본 패키지 설정
1. apt-get => pakage manager
2. 패키지 리스트 추가:  sudo apt-get update 
3. 버전 업그래이드:  sudo apt-get upgrade

#### pyenv 설치

1. https://github.com/yyuu/pyenv-installer 링크로 이동 후 install 명령어 복사 
 $ curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

2. 명령어 수행 후 pyenv 경로 설정

		vi ~/.bash_profile 파일 만든 후 아래 세줄 복사
		export PATH="/home/nick/.pyenv/bin:$PATH"
		eval "$(pyenv init -)"
		eval "$(pyenv virtualenv-init -)"

3. 터미널 재시작 or 다음 명령어 입력:  source ~/.bash_profile
	
		tip) 쉘 스크립트 공부하면 좋아요~!
		~/.bash_profile에 path 및 명령어를 넣어주면 터미널을 생성할 시 자동으로 명령어를 수행하게 해줍니다.
		pyenv 설치 확인: pyenv
		설치 가능 파이썬 버젼 리스트 확인:  pyenv install --list
		파이썬 설치: pyenv install 3.5.2

4. 오류가 발생하면 링크로 가서 필요 패키지 설치 후 다시 파이썬 설치

		설치된 파이썬 버전 확인:  pyenv versions
		원하는 파이썬 버전 실행:  pyenv shell 3.5.2


#### virtualenv 환경 설정

- 언어 관리 => pyenv
- 라이브러리 관리 => virtualenv
- 설정 버젼
	- fastcampus: 3.5.2, django: 1.10
	- stripes: 3.5.2 , django: 1.6

			tip) apt-get, brew, yum => os package manager
			라이브러리 패키지 매니저: python(pip), node(npm), ruby(gem)
			웹 클라이언트 패키지 매니저: bower

1. virtualenv 설치: 설치폴더 이동 후 다음 명령어 입력 
	pyenv virtualenv 3.5.2 fastcampus

2. virtualenv 활성화: pyenv activate fastcampus

3. python package 설치 및 확인: pip install Django==1.8, pip freeze


#### 특정 폴더 접속시 자동 virtualenv 수행(autoenv 설정)

1. autoenv 검색 후 https://github.com/kennethreitz/autoenv로 이동
2. git을 이용한 설치

		$ git clone git://github.com/kennethreitz/autoenv.git ~/.autoenvemphasized text
		$ echo 'source ~/.autoenv/activate.sh' >> ~/.bashrc 
		.bashrc => .bash_profile 로 변경한다.
		
3. 터미널 재시작 or 다음 명령어 입력:  source ~/.bash_profile
4. 각 폴더로 이동 후 .env 파일 생성
5. 파일 안에 activate명령어 입력:  pyenv activate fastcampus

		tip) 리눅스 명령어
		~/ :사용자의 home directory
		. : current folder
		.. : parents folder

		echo "hello world" > hello.txt
		=> 새 파일 생성 후 내용 복사
		echo "hello world second line" >> hello.txt
		=> 기존 파일에 내용 복사

		ps aux | grep python
		ls -al | grep .bash
