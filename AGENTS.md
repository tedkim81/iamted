# 저장소 작업 지침

## 현재 서비스
- `iamted.kim`은 정적 사이트이며, 배포 대상은 `static/html/` 전체이다.
- Django 코드는 deprecated된 과거 구현이다. 일반적인 사이트 수정 요청은 정적 파일 수정으로 해석한다.

## 사이트 수정 위치
- `static/html/index.html`: 메인 페이지. HTML 본문, CSS, 다국어 처리 JavaScript가 모두 들어 있다.
- `static/html/blog_profile.jpg`, `static/html/favicon.ico`: 프로필 사진과 사이트 아이콘.
- `static/html/apps/`: 앱별 페이지와 이미지·영상 등 정적 자산.
- 자기소개는 `index.html`의 `introTextKo`, `introTextEn`을 함께 확인한다.
- `data-i18n` 요소는 로딩 시 텍스트가 덮어써진다. 영어 문구를 변경할 때는 본문, `data-i18n` 값, `translations.ko`의 대응 키와 한국어 번역을 함께 수정한다.
- 문구·레이아웃 수정 후 기본 한국어 화면과 `?lang=en` 영어 화면을 확인한다. Django 실행이나 `collectstatic`은 필요하지 않다.

## Django 코드 보호
- 사용자가 Django 또는 과거 구현의 수정을 명시적으로 요청한 경우에만 아래 파일을 수정한다.
  - `app/` 전체(특히 `app/templates/`), `iamted/`, `mytube/`
  - `manage.py`, `requirements.txt`, `locale/`, `locale_make.sh`, `locale_compile.sh`, `loadenv.sh`, `db.sqlite3`
- 사이트 내용을 바꾸기 위해 Django 템플릿, 모델, 뷰, 번역 파일을 수정하거나 정적 페이지와 동기화하지 않는다.
- deprecated 코드를 임의로 정리·삭제하거나 Django 의존성을 갱신하지 않는다.

## 배포
- `deploy.sh`는 `static/html/`을 S3 버킷 `s3://iamted.kim/`에 동기화한다.
- 일반적인 사이트 수정 요청만으로 커밋·푸시·배포하지 않는다. 사용자가 요청한 경우에 실행한다.
- 배포에는 `--delete`가 포함되어 있으므로 로컬 배포 디렉터리에서 삭제한 파일은 S3에서도 삭제된다.
