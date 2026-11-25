name: QQQ AI Daily Report


on:

  schedule:

    # 매일 오전 7시 (한국시간 KST)
    # GitHub Actions는 UTC 기준
    # UTC 22:00 = KST 07:00
    - cron: "0 22 * * *"


  # GitHub에서 수동 실행 가능
  workflow_dispatch:



jobs:


  qqq-report:


    runs-on: ubuntu-latest


    permissions:

      contents: read



    steps:


      # ==========================
      # 소스 코드 가져오기
      # ==========================

      - name: Checkout Repository

        uses: actions/checkout@v4



      # ==========================
      # Python 환경 설정
      # ==========================

      - name: Setup Python

        uses: actions/setup-python@v5

        with:

          python-version: "3.11"

          cache: "pip"



      # ==========================
      # 라이브러리 설치
      # ==========================

      - name: Install Dependencies

        run: |

          python -m pip install --upgrade pip

          pip install -r requirements.txt



      # ==========================
      # Secret 전달 확인
      # ==========================

      - name: Check Secrets

        env:

          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}

          NAVER_EMAIL: ${{ secrets.NAVER_EMAIL }}

          NAVER_PASSWORD: ${{ secrets.NAVER_PASSWORD }}


        run: |


          if [ -z "$OPENAI_API_KEY" ]; then

            echo "ERROR: OPENAI_API_KEY가 없습니다."

            exit 1

          else

            echo "OPENAI_API_KEY 정상 전달"

          fi



          if [ -z "$NAVER_EMAIL" ]; then

            echo "ERROR: NAVER_EMAIL이 없습니다."

            exit 1

          else

            echo "NAVER_EMAIL 정상 전달"

          fi



          if [ -z "$NAVER_PASSWORD" ]; then

            echo "ERROR: NAVER_PASSWORD가 없습니다."

            exit 1

          else

            echo "NAVER_PASSWORD 정상 전달"

          fi




      # ==========================
      # QQQ AI 리포트 실행
      # ==========================

      - name: Run QQQ AI Report


        env:

          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}

          NAVER_EMAIL: ${{ secrets.NAVER_EMAIL }}

          NAVER_PASSWORD: ${{ secrets.NAVER_PASSWORD }}


        run: |


          python qqq_report.py
