# 개요
제품의 QA 과정에 불필요한 과정을 제거하거나 자동화하여 업무의 효율을 높이기 위함
금번 프로젝트의 주요 기술 스택(및 오픈소스 등)은 다음과 같음
- Docker
- PostgreSQL 
  - Replication
  - Keepalived
- Selenium (IDE)
- monit


# 문제 정의 및 해결 방안
1. 제품을 구성하는 모듈이 관리되는 경로가 정리되어 있지 않음
   - 개발팀과 협의하여 관리 경로를 재정리하고, 이를 문서화하여 공지함
   - 지정된 관리 경로가 아닌 경우 빌드 제한
2. 모듈 간의 호환성을 알 수 없음
3. 테스트 시 모듈 교체에 상당 시간 소요됨
   - 각 관리 경로에서 관리되는 모듈을 자동으로 다운로드하는 방식으로 변경


### 모듈 교체
1. 모듈 교체 스크립트
   - SSRconfig.yaml (모듈에 대한 버전 세팅 파일) 
   - yaml, xml과 같은 config 파일 작성 (ex. Dockerfile)
   - 모든 버전이 적혀야 함
2. read SSRconfig.yaml
3. OS 버전 확인
   - 교체할 모듈 버전과 OS 버전 비교
4. 모듈 백업 및 교체


### Agent 환경 관리 (Dockerfile)
1. OS 버전별 Docker image 관리
   - 다양한 고객사 Agent 설치 환경을 빠르게 재현하기 위함
   - 제품에 사용되는 Debian iamge는 제품용 image로 추가 관리함


### 고객사별 Docker image 관리
1. 고객사별 SSRConfig.yaml 관리 및 Docker image build
   - 패치 시, SSRConfig.yaml을 수정하여 rebuild


### 제품 testing
1. 케이스(및 시나리오) 기반 testing
- FrontEnd testing
  - Selenium을 메인으로 Python 기반 스크립트 작성
- BackEnd testing
  - API testing
    - response 값 종합 및 특정 패턴(필수 데이터가 존재하지 않는 등)이 존재하면 fail 처리