# unityWebSite_django
22년 유니티 게임을 사이트에서 소개

### 접속환경
~/user/signup/
> 회원가입 post 

~/user/api-auth/
> 세션 및 베이직 로그인

~/api-token-auth/
> Post로 로그인시 token 리턴

~/gamerank/
~/gamerank/{int:pk}
> gamerank로 로그인시 post 가능 하며 랭킹고유id를 입력시 해당 랭킹만 Get
> gamerank로 get시 서버에 저장된 랭킹 모두 출력

### my_settings.py 생성
DB연결과 장고프로젝트 키를 저장하는 별도의 파일을 생성하여 사용합니다.
