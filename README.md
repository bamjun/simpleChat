# Django simple chatting web app

# todo list
1. create venv  
2. create a.sh for venv  
3. create django forder  
  $ pip install django  
  $ django-admin startproject config .    
4. make app for main screen of chat.  
  $ django-admin startapp chat  
5. make urls.py on chatFolder and connect from configUrls to chatUrls  
6. create hello page  
7. install channels and daphne  
  $ python -m pip install -U channels  
  $ python -m pip install -U daphne





  
#
#
#
# to do when integration with aws
Daphne는 Django Channels의 중요한 컴포넌트 중 하나로, ASGI(Asynchronous Server Gateway Interface) 서버입니다. 기존의 Django는 WSGI(Web Server Gateway Interface)를 사용하여 요청을 처리하는 동기적 서버를 사용했습니다. 그러나 Django Channels의 도입으로 비동기 처리가 필요해졌고, 이를 위해 ASGI 서버인 Daphne가 사용됩니다.

### Daphne의 주요 기능

1. **비동기 처리 지원**: Daphne는 비동기 프로토콜인 ASGI를 지원합니다. 이를 통해 웹소켓, HTTP2, 기타 비동기 프로토콜을 처리할 수 있습니다.

2. **웹소켓 연결 관리**: 웹소켓은 Daphne의 핵심 기능 중 하나로, 실시간 양방향 통신을 가능하게 합니다. 이를 통해 채팅 애플리케이션, 실시간 알림 등을 구현할 수 있습니다.

3. **Channels와의 통합**: Daphne는 Django Channels와 긴밀하게 통합되어 있으며, Channels에서 정의된 라우팅 및 채널 레이어와 함께 작동합니다.

4. **확장성 및 성능**: Daphne는 동시에 여러 연결을 처리할 수 있으며, 다양한 환경에서의 확장성과 성능을 제공합니다.

### 설치 및 사용

Daphne는 pip를 통해 설치할 수 있습니다:

```bash
pip install daphne
```

설치 후, Django 프로젝트의 ASGI 애플리케이션을 Daphne 서버를 사용하여 실행할 수 있습니다. 예를 들어, 프로젝트의 `asgi.py` 파일을 사용하여 Daphne 서버를 시작하는 명령은 다음과 같습니다:

```bash
daphne -p 8001 myproject.asgi:application
```

이 명령은 8001 포트에서 `myproject`의 ASGI 애플리케이션을 Daphne 서버를 사용하여 실행합니다.

### 주의사항

Daphne는 프로덕션 환경에서 사용될 때, 보통 Nginx 같은 리버스 프록시 뒤에 위치합니다. 이는 보안과 성능 최적화를 위해 중요합니다. Nginx는 정적 파일을 처리하고, HTTPS를 관리하는 등의 역할을 수행하며, 실제 ASGI 요청은 Daphne로 전달됩니다.

Daphne는 Django Channels와 함께 사용할 때 Django 애플리케이션에 비동기 및 실시간 기능을 제공하는 강력한 도구입니다.