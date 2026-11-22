# -*- coding: utf-8 -*-
"""Chunk 3 판정 결과 직렬화 (판정 자체는 세션의 개별 판독으로 완료됨 - 이 스크립트는 저장만 함)."""
import json
import os
import sys

RUN = r"C:\Users\h0912\Sharefolder\Claude_project\GLM_SAAS_WORD\output\_pipeline\runs\RUN-20261122-140232-KST"
REQ = os.path.join(RUN, "judgment", "review_titles_chunk3_round1_request.json")
OUT = os.path.join(RUN, "tmp", "decisions", "_chunk3_decisions.json")

# title -> (approve, confidence, reason)  /  checks는 승인=모두 true, 기각=clarity false로 고정
V = {
    # === 사전·학습 조회 관용구 승인 (Syllables/Rhymes/Synonyms/Antonyms/Sentences/Translations/Anagrams/Orthography) ===
    "Flashcard Orthography": (True, 0.8, "'Flashcard' 학습 도메인에 철자 조회 관용구 'Orthography'를 얹은 사전 조회형 도구로 읽히고, 배치 내 중복·상표 요인 없음."),
    "Material Syllables": (True, 0.8, "'Material'이라는 단어의 음절 조회로 읽히는 사전 쿼리 결합으로 명확하고 중복·상표 없음."),
    "Storefront Rhymes": (True, 0.8, "'Storefront'의 라임 조회 관용구로 사전 조회 도구가 명확하고, 배치 내 동의어 겹침·상표 없음."),
    "Booking Synonyms": (True, 0.8, "'Booking'의 유의어 조회로 읽히며 명확하고 중복·상표 없음."),
    "Syllabus Antonyms": (True, 0.8, "'Syllabus'의 반의어 조회 관용구 결합으로 명확하고 중복·상표 없음."),
    "Batch Sentences": (True, 0.8, "'Batch'라는 단어의 예문 조회로 읽히는 결합으로 명확·비중복·상표 무관."),
    "Grazing Translations": (True, 0.8, "'Grazing'의 번역 조회 관용구로 사전/번역 도구가 연상되고 중복·상표 없음."),
    "Impact Anagrams": (True, 0.8, "'Impact'의 애나그램 조회로 명확한 사전 쿼리 결합이며 중복·상표 없음."),
    "Licensing Orthography": (True, 0.8, "'Licensing'의 철자 조회 관용구로 명확하고 중복·상표 없음."),
    "Leaf Syllables": (True, 0.8, "'Leaf'의 음절 조회로 읽히는 결합으로 명확·비중복·상표 무관."),
    "Clinic Rhymes": (True, 0.8, "'Clinic'의 라임 조회 관용구로 명확하고 배치 내 중복·상표 없음."),
    "Attorney Antonyms": (True, 0.8, "'Attorney'의 반의어 조회로 명확한 사전 쿼리이며 중복·상표 없음."),
    "Consignee Sentences": (True, 0.8, "'Consignee'의 예문 조회 관용구 결합으로 명확하고 중복·상표 없음."),
    "Rezoning Translations": (True, 0.8, "'Rezoning'의 번역 조회로 읽히며 명확하고 중복·상표 없음."),
    "Bonus Anagrams": (True, 0.8, "'Bonus'의 애나그램 조회 관용구로 명확·비중복·상표 무관."),
    "Credit Orthography": (True, 0.8, "'Credit'의 철자 조회로 읽히는 사전 쿼리 결합이며 중복·상표 없음."),
    "Editor Syllables": (True, 0.8, "'Editor'의 음절 조회 관용구로 명확하고 중복·상표 없음."),
    "Contact Rhymes": (True, 0.8, "'Contact'의 라임 조회로 명확한 사전 쿼리이며 중복·상표 없음."),
    "Portfolio Synonyms": (True, 0.8, "'Portfolio'의 유의어 조회 관용구 결합으로 명확·비중복·상표 무관."),
    "Checkin Antonyms": (True, 0.8, "'Checkin'의 반의어 조회로 읽히며 명확하고 중복·상표 없음."),
    "Headlight Sentences": (True, 0.8, "'Headlight'의 예문 조회 관용구로 명확하고 중복·상표 없음."),
    "Brunch Translations": (True, 0.8, "'Brunch'의 번역 조회로 명확한 사전 쿼리 결합이며 중복·상표 없음."),
    "Cleaning Anagrams": (True, 0.8, "'Cleaning'의 애나그램 조회 관용구로 명확·비중복·상표 무관."),
    "Tree Orthography": (True, 0.8, "'Tree'의 철자 조회로 읽히는 결합으로 명확하고 중복·상표 없음."),
    "Migraine Syllables": (True, 0.8, "'Migraine'의 음절 조회 관용구로 명확·비중복·상표 무관."),
    "Rebate Rhymes": (True, 0.8, "'Rebate'의 라임 조회로 명확한 사전 쿼리이며 중복·상표 없음."),
    "Homeschool Synonyms": (True, 0.8, "'Homeschool'의 유의어 조회 관용구 결합으로 명확·비중복·상표 무관."),
    "Anniversary Antonyms": (True, 0.8, "'Anniversary'의 반의어 조회로 읽히며 명확하고 중복·상표 없음."),
    "Kebab Sentences": (True, 0.8, "'Kebab'의 예문 조회 관용구로 명확하고 중복·상표 없음."),
    "Groomer Translations": (True, 0.8, "'Groomer'의 번역 조회로 명확한 사전 쿼리 결합이며 중복·상표 없음."),
    "Intercom Anagrams": (True, 0.8, "'Intercom'의 애나그램 조회 관용구로 명확·비중복·상표 무관."),
    "Reserve Orthography": (True, 0.8, "'Reserve'의 철자 조회로 읽히는 결합으로 명확하고 중복·상표 없음."),
    "Payroll Syllables": (True, 0.8, "'Payroll'의 음절 조회 관용구로 명확·비중복·상표 무관."),
    "Material Rhymes": (True, 0.8, "'Material'의 라임 조회로 명확하고, 같은 앵커의 Syllables와 조회 절이 달라 중복이 아니며 상표 없음."),
    "Storefront Synonyms": (True, 0.8, "'Storefront'의 유의어 조회 관용구로 Rhymes·Antonyms와 결이 달라 중복이 아니고 상표 없음."),
    "Booking Antonyms": (True, 0.8, "'Booking'의 반의어 조회로 명확하고, Synonyms와 별개 조회절이라 중복이 아니며 상표 없음."),
    "Syllabus Sentences": (True, 0.8, "'Syllabus'의 예문 조회 관용구로 명확·비중복·상표 무관."),
    "Batch Translations": (True, 0.8, "'Batch'의 번역 조회로 명확한 사전 쿼리 결합이며 중복·상표 없음."),
    "Demand Anagrams": (True, 0.8, "'Demand'의 애나그램 조회 관용구로 명확하고 중복·상표 없음."),
    "Referral Orthography": (True, 0.8, "'Referral'의 철자 조회로 읽히며 명확하고 중복·상표 없음."),
    "Chess Syllables": (True, 0.8, "'Chess'의 음절 조회 관용구로 명확·비중복·상표 무관."),
    "Leaf Rhymes": (True, 0.8, "'Leaf'의 라임 조회로 명확하고, 같은 앵커의 Syllables와 별개 조회절이라 중복이 아니며 상표 없음."),
    "Clinic Synonyms": (True, 0.8, "'Clinic'의 유의어 조회 관용구로 명확하고 중복·상표 없음."),
    "Attorney Sentences": (True, 0.8, "'Attorney'의 예문 조회로 명확한 사전 쿼리이며 중복·상표 없음."),
    "Consignee Translations": (True, 0.8, "'Consignee'의 번역 조회 관용구 결합으로 명확·비중복·상표 무관."),
    "Loss Anagrams": (True, 0.8, "'Loss'의 애나그램 조회로 명확하고 중복·상표 없음."),
    "Thrift Orthography": (True, 0.8, "'Thrift'의 철자 조회 관용구로 명확하고 중복·상표 없음."),
    "Sidewalk Syllables": (True, 0.8, "'Sidewalk'의 음절 조회로 읽히는 결합으로 명확·비중복·상표 무관."),
    "Editor Rhymes": (True, 0.8, "'Editor'의 라임 조회 관용구로 명확하고 중복·상표 없음."),
    "Contact Synonyms": (True, 0.8, "'Contact'의 유의어 조회로 명확하고, Rhymes와 별개 조회절이라 중복이 아니며 상표 없음."),
    "Portfolio Antonyms": (True, 0.8, "'Portfolio'의 반의어 조회 관용구로 명확·비중복·상표 무관."),
    "Checkin Sentences": (True, 0.8, "'Checkin'의 예문 조회로 읽히며 명확하고 중복·상표 없음."),
    "Headlight Translations": (True, 0.8, "'Headlight'의 번역 조회 관용구로 명확하고 중복·상표 없음."),
    "Shelter Anagrams": (True, 0.8, "'Shelter'의 애나그램 조회로 명확한 사전 쿼리 결합이며 중복·상표 없음."),
    "Nap Orthography": (True, 0.8, "'Nap'의 철자 조회 관용구로 명확·비중복·상표 무관."),
    "Desert Syllables": (True, 0.8, "'Desert'의 음절 조회로 명확하고 중복·상표 없음."),
    "Migraine Rhymes": (True, 0.8, "'Migraine'의 라임 조회 관용구로 Syllables와 별개 조회절이라 중복이 아니고 상표 없음."),
    "Rebate Synonyms": (True, 0.8, "'Rebate'의 유의어 조회로 명확하고 중복·상표 없음."),
    "Homeschool Antonyms": (True, 0.8, "'Homeschool'의 반의어 조회 관용구로 명확하고 중복·상표 없음."),
    "Anniversary Sentences": (True, 0.8, "'Anniversary'의 예문 조회로 읽히는 결합으로 명확·비중복·상표 무관."),
    "Kebab Translations": (True, 0.8, "'Kebab'의 번역 조회 관용구로 명확하고 중복·상표 없음."),
    "Malocclusion Anagrams": (True, 0.8, "'Malocclusion'의 애나그램 조회로 명확한 사전 쿼리이며 중복·상표 없음."),
    "Insomnia Orthography": (True, 0.8, "'Insomnia'의 철자 조회 관용구로 명확·비중복·상표 무관."),
    "Subrogation Syllables": (True, 0.8, "'Subrogation'의 음절 조회로 읽히며 명확하고 중복·상표 없음."),
    "Payroll Rhymes": (True, 0.8, "'Payroll'의 라임 조회 관용구로 Syllables와 별개 조회절이라 중복이 아니고 상표 없음."),
    "Material Synonyms": (True, 0.8, "'Material'의 유의어 조회로 명확하고 중복·상표 없음."),
    "Storefront Antonyms": (True, 0.8, "'Storefront'의 반의어 조회 관용구로 명확하고 중복·상표 없음."),
    "Booking Sentences": (True, 0.8, "'Booking'의 예문 조회로 명확한 사전 쿼리 결합이며 중복·상표 없음."),
    "Syllabus Translations": (True, 0.8, "'Syllabus'의 번역 조회 관용구로 명확·비중복·상표 무관."),
    "Grazing Anagrams": (True, 0.8, "'Grazing'의 애나그램 조회로 명확하고 중복·상표 없음."),
    "Oboe Syllables": (True, 0.8, "'Oboe'의 음절 조회 관용구로 명확·비중복·상표 무관."),
    "Chess Rhymes": (True, 0.8, "'Chess'의 라임 조회로 명확하고, 같은 앵커의 Syllables와 별개 조회절이라 중복이 아니며 상표 없음."),
    "Leaf Synonyms": (True, 0.8, "'Leaf'의 유의어 조회 관용구로 명확하고 중복·상표 없음."),
    "Clinic Antonyms": (True, 0.8, "'Clinic'의 반의어 조회로 명확한 사전 쿼리이며 중복·상표 없음."),
    "Attorney Translations": (True, 0.8, "'Attorney'의 번역 조회 관용구로 명확·비중복·상표 무관."),
    "Rezoning Anagrams": (True, 0.8, "'Rezoning'의 애나그램 조회로 읽히며 명확하고 중복·상표 없음."),
    "Electrical Orthography": (True, 0.8, "'Electrical'의 철자 조회 관용구로 명확하고 중복·상표 없음."),
    "Detention Syllables": (True, 0.8, "'Detention'의 음절 조회로 명확한 사전 쿼리 결합이며 중복·상표 없음."),
    "Sidewalk Rhymes": (True, 0.8, "'Sidewalk'의 라임 조회 관용구로 명확·비중복·상표 무관."),
    "Editor Synonyms": (True, 0.8, "'Editor'의 유의어 조회로 명확하고 중복·상표 없음."),
    "Contact Antonyms": (True, 0.8, "'Contact'의 반의어 조회 관용구로 명확·비중복·상표 무관."),
    "Portfolio Sentences": (True, 0.8, "'Portfolio'의 예문 조회로 읽히며 명확하고 중복·상표 없음."),
    "Checkin Translations": (True, 0.8, "'Checkin'의 번역 조회 관용구로 명확하고 중복·상표 없음."),
    "Brunch Anagrams": (True, 0.8, "'Brunch'의 애나그램 조회로 명확한 사전 쿼리 결합이며 중복·상표 없음."),
    "Boxing Orthography": (True, 0.8, "'Boxing'의 철자 조회 관용구로 명확·비중복·상표 무관."),
    "Key Syllables": (True, 0.8, "'Key'의 음절 조회로 명확하고 중복·상표 없음."),
    "Desert Rhymes": (True, 0.8, "'Desert'의 라임 조회 관용구로 Syllables와 별개 조회절이라 중복이 아니고 상표 없음."),
    "Migraine Synonyms": (True, 0.8, "'Migraine'의 유의어 조회로 명확하고 중복·상표 없음."),
    "Rebate Antonyms": (True, 0.8, "'Rebate'의 반의어 조회 관용구로 명확하고 중복·상표 없음."),
    "Homeschool Sentences": (True, 0.8, "'Homeschool'의 예문 조회로 읽히는 결합으로 명확·비중복·상표 무관."),
    "Anniversary Translations": (True, 0.8, "'Anniversary'의 번역 조회 관용구로 명확하고 중복·상표 없음."),
    "Groomer Anagrams": (True, 0.8, "'Groomer'의 애나그램 조회로 명확한 사전 쿼리이며 중복·상표 없음."),
    # === Chords/Lyrics 계열 - 개별 판독 ===
    "Insomnia Chords": (True, 0.65, "불면 완화용 코드·앰비언트 연주 앱으로 읽히는 'Insomnia'+'Chords' 결합으로 실제 서비스 대상이 그려지고 중복·상표 없음. 음악 해석이 우세한지는 약간 애매해 신뢰도 보통."),
    "Nap Lyrics": (True, 0.6, "'Nap' 낮잠 시간용 자장가·가사 콘텐츠 도구로 읽힐 여지가 있어 승인하나 해석이 한쪽으로 몰리지 않아 신뢰도 낮음."),
    "Demand Conjugations": (True, 0.65, "'to demand'의 동사 활용 조회로 읽히는 'Conjugations' 관용구 결합으로 명확하고 중복·상표 없음."),
    "Grazing Conjugations": (True, 0.6, "'graze' 동사의 활용 조회로 해석 가능해 승인하나 'Grazing'이 목초지 명사로 먼저 읽히는 애매함이 있음."),
    "Shelter Conjugations": (True, 0.62, "'to shelter' 동사의 활용 조회 관용구로 명확하고 중복·상표 없음."),
    "Rezoning Conjugations": (True, 0.55, "'rezone' 동사의 활용 조회로 극단적으로 해석 가능하나 'Rezoning'이 명사(구역재개발)로 읽히는 힘이 강해 신뢰도 낮음."),
    "Batch Conjugations": (True, 0.55, "'to batch' 동사 활용 조회로도 읽히나 기술 용법이라 일반 이해도가 낮아 신뢰도 낮게 승인."),
    # === 음식 도메인 + 서비스 기능어 승인 ===
    "Bruschetta Rendering": (True, 0.6, "'Bruschetta' 음식 3D 렌더링·메뉴 이미지 생성 도구로 읽히고 중복·상표 없음."),
    "Prosciutto Kit": (True, 0.7, "'Prosciutto' 밀 키트·준비 키트 서비스로 명확한 결합이며 중복·상표 없음."),
    "Edamame Widget": (True, 0.65, "'Edamame' 판매·주문 위젯으로 읽히는 구체 기능 결합이며 중복·상표 없음."),
    "Ceviche Announcement": (True, 0.6, "'Ceviche' 신메뉴 공지·출시 알림 도구로 읽히며 중복·상표 없음."),
    "Bratwurst Checker": (True, 0.65, "'Bratwurst' 굽기 완성도·신선도 확인 도구로 명확하고 중복·상표 없음."),
    "Escargot Timer": (True, 0.7, "'Escargot' 조리 타이머로 읽히는 실용 결합이며 중복·상표 없음."),
    "Gyro Guardian": (True, 0.6, "'Gyro' 위생·보관 상태 감시 도구로 읽히는 은유+기능 결합이며 중복·상표 없음."),
    "Satay Streak": (True, 0.6, "'Satay' 연속 판매·식단 기록 스트릭 추적으로 읽히고 중복·상표 없음."),
    "Moussaka Rank": (True, 0.6, "'Moussaka' 메뉴 순위·평판 랭킹 도구로 읽히며 중복·상표 없음."),
    "Borscht Trend": (True, 0.65, "'Borscht' 메뉴 트렌드 분석 도구로 명확한 결합이며 중복·상표 없음."),
    "Gumbo Comparison": (True, 0.6, "'Gumbo' 메뉴·레시피 비교 도구로 읽히고 중복·상표 없음."),
    "Jambalaya Proposal": (True, 0.65, "'Jambalaya' 케이터링 제안서 작성 도구로 읽히며 중복·상표 없음."),
    "Shawarma Guarantee": (True, 0.6, "'Shawarma' 품질·신선도 보증 관리 도구로 읽히고 중복·상표 없음."),
    "Naan Record": (True, 0.65, "'Naan' 생산·품질 기록부로 읽히는 결합으로 명확하고 중복·상표 없음."),
    "Arepa Copy": (True, 0.6, "'Arepa' 메뉴·마케팅 카피 생성 도구로 읽히며 중복·상표 없음."),
    "Goulash Reference": (True, 0.65, "'Goulash' 레시피·자료 참조 라이브러리로 읽히고 중복·상표 없음."),
    "Tzatziki Forecast": (True, 0.65, "'Tzatziki' 수요 예측 도구로 명확한 기능 결합이며 중복·상표 없음."),
    "Bruschetta Notification": (True, 0.65, "'Bruschetta' 주문 준비·재고 알림 도구로 읽히고 중복·상표 없음."),
    "Prosciutto Count": (True, 0.65, "'Prosciutto' 재고 수량 카운트 도구로 읽히며 중복·상표 없음."),
    "Tabbouleh Total": (True, 0.6, "'Tabbouleh' 주문 합계·정산 도구로 읽히나 'Total'이 다소 막연해 신뢰도 보통."),
    "Edamame Repository": (True, 0.65, "'Edamame' 레시피·자료 저장소로 읽히는 결합이며 중복·상표 없음."),
    "Ceviche Calculator": (True, 0.7, "'Ceviche' 레시피·영양·원가 계산기로 명확하고 중복·상표 없음."),
    "Guacamole Generator": (True, 0.6, "'Guacamole' 레시피 변형 생성기로 읽히고 중복·상표 없음."),
    "Empanada Estimator": (True, 0.65, "'Empanada' 케이터링 수량·원가 추정기로 읽히며 중복·상표 없음."),
    "Bratwurst Detector": (True, 0.6, "'Bratwurst' 익힘·이물 감지 도구로 읽히며 Checker와 결이 달라 독립 기능으로 보고 중복 아님, 상표 없음."),
    "Escargot Workshop": (True, 0.65, "'Escargot' 요리 워크숍 예약·운영 도구로 명확하고 중복·상표 없음."),
    "Mochi Streak": (True, 0.6, "'Mochi' 연속 기록 스트릭 추적으로 읽히고 중복·상표 없음."),
    "Satay Rank": (True, 0.6, "'Satay' 메뉴 순위 도구로 읽히며 Streak와 기능이 달라 중복이 아니고 상표 없음."),
    "Moussaka Trend": (True, 0.65, "'Moussaka' 트렌드 분석으로 명확하고 Rank와 결이 달라 중복이 아니며 상표 없음."),
    "Borscht Comparison": (True, 0.6, "'Borscht' 메뉴 비교 도구로 읽히고 Trend와 별개 기능이라 중복이 아니며 상표 없음."),
    "Gumbo Proposal": (True, 0.65, "'Gumbo' 케이터링 제안 도구로 읽히며 중복·상표 없음."),
    "Jambalaya Guarantee": (True, 0.6, "'Jambalaya' 품질 보증 관리로 읽히고 중복·상표 없음."),
    "Shawarma Record": (True, 0.65, "'Shawarma' 생산·판매 기록 장부로 명확하고 Guarantee와 별개 기능이라 중복이 아니며 상표 없음."),
    "Naan Copy": (True, 0.6, "'Naan' 메뉴 카피 생성 도구로 읽히며 Record와 결이 달라 중복이 아니고 상표 없음."),
    "Pierogi Reference": (True, 0.65, "'Pierogi' 레시피 참고 자료실로 읽히고 중복·상표 없음."),
    "Goulash Forecast": (True, 0.65, "'Goulash' 수요 예측 도구로 명확하고 Reference와 별개 기능이라 중복이 아니며 상표 없음."),
    "Tzatziki Deadline": (True, 0.6, "'Tzatziki' 조리·준비 기한 관리 도구로 읽히고 중복·상표 없음."),
    "Acai Rendering": (True, 0.6, "'Acai' 볼 3D 렌더링·메뉴 이미지 도구로 읽히며 중복·상표 없음. Sketch·Outline과 달리 'Rendering'은 구체 산출물을 지시."),
    "Bruschetta Kit": (True, 0.7, "'Bruschetta' 밀 키트 서비스로 명확하고 중복·상표 없음."),
    "Tabbouleh Widget": (True, 0.65, "'Tabbouleh' 주문·예약 위젯으로 읽히고 중복·상표 없음."),
    "Edamame Announcement": (True, 0.6, "'Edamame' 입고·신메뉴 알림 발송 도구로 읽히며 Widget과 별개 기능이라 중복이 아니고 상표 없음."),
    "Empanada Checker": (True, 0.6, "'Empanada' 익힘·품질 확인 도구로 읽히고 Bratwurst Checker와 앵커가 달라 별개 제품이며 상표 없음."),
    "Bratwurst Timer": (True, 0.7, "'Bratwurst' 굽기 타이머로 명확한 실용 결합이며 Checker·Detector와 기능이 달라 중복이 아니고 상표 없음."),
    "Escargot Guardian": (True, 0.6, "'Escargot' 보관·위생 감시 도구로 읽히고 Timer와 별개 기능이라 중복이 아니며 상표 없음."),
    "Quinoa Streak": (True, 0.6, "'Quinoa' 식단 연속 기록 스트릭으로 읽히고 중복·상표 없음."),
    "Mochi Rank": (True, 0.6, "'Mochi' 메뉴 순위 도구로 읽히며 Streak와 별개 기능이라 중복이 아니고 상표 없음."),
    "Satay Trend": (True, 0.65, "'Satay' 트렌드 분석으로 명확하고 Rank·Streak와 결이 달라 중복이 아니며 상표 없음."),
    "Moussaka Comparison": (True, 0.6, "'Moussaka' 메뉴 비교 도구로 읽히고 중복·상표 없음."),
    "Borscht Proposal": (True, 0.65, "'Borscht' 케이터링 제안서 도구로 읽히며 중복·상표 없음."),
    "Gumbo Guarantee": (True, 0.6, "'Gumbo' 품질 보증 관리로 읽히고 중복·상표 없음."),
    "Jambalaya Record": (True, 0.65, "'Jambalaya' 제조·판매 기록 장부로 명확하고 Proposal·Guarantee와 별개 기능이라 중복이 아니며 상표 없음."),
    "Shawarma Copy": (True, 0.6, "'Shawarma' 메뉴 카피 생성으로 읽히고 Record와 별개 기능이라 중복이 아니며 상표 없음."),
    "Arepa Reference": (True, 0.65, "'Arepa' 레시피 참고 자료실로 읽히고 중복·상표 없음."),
    "Pierogi Forecast": (True, 0.65, "'Pierogi' 수요 예측 도구로 명확하고 Reference와 별개 기능이라 중복이 아니며 상표 없음."),
    "Goulash Deadline": (True, 0.6, "'Goulash' 준비 기한 관리로 읽히고 중복·상표 없음."),
    "Tzatziki Duration": (True, 0.6, "'Tzatziki' 숙성·조리 시간 추적으로 읽히며 중복·상표 없음."),
    # === 기각 ===
    "Reserve Lyrics": (False, 0.7, "'Reserve'와 가사 'Lyrics'의 결합이 어떤 서비스 기능도 지시하지 못함 - 준비금과 가사는 결합 대상이 성립하지 않아 명확성 탈락."),
    "Acai Sketch": (False, 0.65, "'Acai' 볼 업계에서 'Sketch'가 무엇을 그리는지 서비스 대상이 만들어지지 않음(과거 'Acai Extension' 기각과 같은 결) - 명확성 탈락."),
    "Tabbouleh Message": (False, 0.65, "'Tabbouleh'에 'Message'가 어떤 메시지를 누구에게 보내는지 불명확해 서비스 대상이 성립하지 않음 - 명확성 탈락."),
    "Guacamole Converter": (False, 0.6, "'Guacamole Converter'는 무엇을 무엇으로 변환하는지 불명확해 기능 대상이 성립하지 않음 - 명확성 탈락."),
    "Empanada Recorder": (False, 0.65, "'Empanada'와 'Recorder'의 결합은 무엇을 녹음·기록하는지 불명확해 서비스가 그려지지 않음 - 명확성 탈락."),
    "Quinoa Stage": (False, 0.6, "'Quinoa Stage'가 조리 단계인지 무대인지 해석이 갈리고 어떤 기능도 지시하지 못해 명확성 탈락."),
    "Mochi Result": (False, 0.65, "'Mochi Result'는 무엇의 결과인지 불명확해 제품 기능이 성립하지 않음 - 명확성 탈락."),
    "Pierogi Reading": (False, 0.6, "'Pierogi'에 'Reading'이 온도 계량인지 열람인지 불명확하고 실제 서비스 대상이 만들어지지 않음 - 명확성 탈락."),
    "Referral Lyrics": (False, 0.7, "'Referral'과 가사 'Lyrics'는 결합해도 서비스 기능이 성립하지 않음 - 명확성 탈락."),
    "Loss Conjugations": (False, 0.75, "'Loss'는 동사가 없는 명사라 활용 조회 'Conjugations'와 결합해도 조회 대상이 성립하지 않음 - 명확성 탈락."),
    "Electrical Chords": (False, 0.7, "'Electrical'은 전기 공사 도메인이라 코드 'Chords'와의 결합이 전기 서비스에서 성립하지 않고 음악 해석도 앵커와 어긋남 - 명확성 탈락."),
    "Thrift Lyrics": (False, 0.7, "'Thrift' 중고 판매 도메인과 가사 'Lyrics'는 서비스 대상이 만들어지지 않는 결합 - 명확성 탈락."),
    "Boxing Chords": (False, 0.7, "'Boxing' 권투 도메인에 코드 'Chords'가 붙어도 어떤 제품도 성립하지 않음 - 명확성 탈락."),
    "Malocclusion Conjugations": (False, 0.75, "'Malocclusion'은 부정교합 명사로 동사 활용이 없어 'Conjugations' 조회 대상이 성립하지 않음 - 명확성 탈락."),
    "Winery Chords": (False, 0.6, "'Winery'와 코드 'Chords'의 결합은 와이너리 공연 코드 검색 같은 해석도 억지스러워 서비스 대상이 불분명 - 명확성 탈락."),
    "Insomnia Lyrics": (False, 0.65, "불면과 가사 'Lyrics'의 결합은 'Insomnia Chords'와 달리 가사로 만들어지는 서비스 기능이 떠오르지 않음 - 명확성 탈락."),
    "Acai Outline": (False, 0.65, "'Acai'에 'Outline'이 무엇의 개요·윤곽인지 불명확해 서비스가 성립하지 않음 - 명확성 탈락."),
    "Gyro Helper": (False, 0.6, "'Helper'가 무엇을 도와주는지 구체 기능 없이 막연해 'Gyro Helper'는 서비스 대상이 성립하지 않음 - 명확성 탈락."),
    "Quinoa Result": (False, 0.65, "'Quinoa Result'는 무엇의 결과인지 불명확해 기능이 성립하지 않음 - 명확성 탈락."),
    "Arepa Reading": (False, 0.6, "'Arepa'와 'Reading'의 결합은 계량·열람 어느 쪽도 서비스로 성립하지 않음 - 명확성 탈락."),
    "Impact Chords": (False, 0.7, "'Impact'와 코드 'Chords'는 비영리 도메인에서 서비스 대상이 만들어지지 않음 - 명확성 탈락."),
    "Bonus Chords": (False, 0.7, "'Bonus'와 코드 'Chords'의 결합은 급여 도메인에서 아무 기능도 성립하지 않음 - 명확성 탈락."),
    "Electrical Lyrics": (False, 0.7, "'Electrical' 전기 도메인과 가사 'Lyrics'는 결합 대상이 성립하지 않음 - 명확성 탈락."),
    "Brunch Conjugations": (False, 0.75, "'Brunch'는 동사가 없는 명사라 활용 조회 'Conjugations'와 결합할 대상이 없음 - 명확성 탈락."),
    "Cleaning Chords": (False, 0.65, "'Cleaning' 도메인에 코드 'Chords'가 붙어도 청소 서비스에서 성립하지 않음 - 명확성 탈락."),
    "Boxing Lyrics": (False, 0.7, "'Boxing' 권투와 가사 'Lyrics'는 서비스 대상이 만들어지지 않음 - 명확성 탈락."),
    "Groomer Conjugations": (False, 0.75, "'Groomer'는 명사(미용사)라 동사 활용 조회 'Conjugations'의 대상이 될 수 없음 - 명확성 탈락."),
    "Intercom Chords": (False, 0.6, "'Intercom' 인터폰 도메인에 코드 'Chords'를 얹으면 서비스가 성립하지 않음 - 명확성 탈락."),
    "Winery Lyrics": (False, 0.65, "'Winery'와 가사 'Lyrics'의 결합은 와이너리 도메인에서 서비스 대상이 불명확 - 명확성 탈락."),
    "Prosciutto Message": (False, 0.65, "'Prosciutto'에 'Message'가 어떤 발신 기능인지 불명확해 서비스가 성립하지 않음 - 명확성 탈락."),
    "Ceviche Converter": (False, 0.6, "'Ceviche Converter'는 무엇을 변환하는지 불명확해 기능 대상이 성립하지 않음 - 명확성 탈락."),
    "Guacamole Recorder": (False, 0.65, "'Guacamole'과 'Recorder'의 결합은 기록 대상이 불명확해 서비스가 그려지지 않음 - 명확성 탈락."),
    "Gyro Stage": (False, 0.6, "'Gyro Stage'는 공연 무대인지 조리 단계인지 해석이 갈라지고 기능이 성립하지 않음 - 명확성 탈락."),
    "Naan Reading": (False, 0.6, "'Naan'과 'Reading'의 결합은 온도 계량·열람 어느 쪽도 서비스로 성립하지 않음 - 명확성 탈락."),
    "Demand Chords": (False, 0.7, "'Demand' 전력 수요 도메인과 코드 'Chords'는 결합 대상이 성립하지 않음 - 명확성 탈락."),
    "Impact Lyrics": (False, 0.7, "'Impact'와 가사 'Lyrics'는 비영리 도메인에서 서비스가 만들어지지 않음 - 명확성 탈락."),
    "Consignee Conjugations": (False, 0.75, "'Consignee'는 수취인 명사로 활용 조회 'Conjugations'의 대상이 될 수 없음 - 명확성 탈락."),
    "Loss Chords": (False, 0.7, "'Loss' 보험 도메인과 코드 'Chords'는 서비스 대상이 성립하지 않음 - 명확성 탈락."),
    "Bonus Lyrics": (False, 0.7, "'Bonus'와 가사 'Lyrics'의 결합은 급여 도메인에서 기능이 성립하지 않음 - 명확성 탈락."),
    "Headlight Conjugations": (False, 0.75, "'Headlight'는 부품 명사라 동사 활용 조회 'Conjugations'의 대상이 될 수 없음 - 명확성 탈락."),
    "Shelter Chords": (False, 0.65, "'Shelter'와 코드 'Chords'의 결합은 보호소 도메인에서 서비스가 성립하지 않음 - 명확성 탈락."),
    "Cleaning Lyrics": (False, 0.65, "'Cleaning' 도메인과 가사 'Lyrics'는 서비스 대상이 만들어지지 않음 - 명확성 탈락."),
    "Kebab Conjugations": (False, 0.75, "'Kebab'은 음식 명사로 활용 조회 'Conjugations'의 대상이 될 수 없음 - 명확성 탈락."),
    "Malocclusion Chords": (False, 0.65, "'Malocclusion' 치과 용어와 코드 'Chords'는 결합 대상이 성립하지 않음 - 명확성 탈락."),
    "Intercom Lyrics": (False, 0.65, "'Intercom'과 가사 'Lyrics'의 결합은 인터폰 도메인에서 기능이 성립하지 않음 - 명확성 탈락."),
}


def main():
    with open(REQ, encoding="utf-8") as f:
        req = json.load(f)
    items = req["items"]
    titles = [it["title"] for it in items]
    assert len(items) == 200, len(items)
    assert len(set(titles)) == 200
    missing = [t for t in titles if t not in V]
    extra = [t for t in V if t not in set(titles)]
    if missing or extra:
        print("MISSING:", missing)
        print("EXTRA:", extra)
        sys.exit(1)
    out = []
    for t in titles:
        approve, conf, reason = V[t]
        checks = {"clarity": approve, "duplication": True, "trademark": True}
        out.append({
            "title": t,
            "approve": approve,
            "confidence": conf,
            "reason": reason,
            "checks": checks,
        })
    approved = sum(1 for d in out if d["approve"])
    rejected = len(out) - approved
    # 논리 불일치 자가검증: approve=true면 checks 전부 true
    for d in out:
        ok = all(d["checks"].values()) if d["approve"] else not d["checks"]["clarity"]
        assert ok, d["title"]
    tmp = OUT + ".tmp"
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write("\n")
    os.replace(tmp, OUT)
    print("saved:", OUT, "items:", len(out), "approved:", approved, "rejected:", rejected)


if __name__ == "__main__":
    main()
