/* Content authority: latest MD. V2 changes visual composition. */
window.EONU.slides = [
  {
    "id": "01",
    "section": "INTRODUCTION",
    "title": "이어지는 진료, <em>세 사람의 안심</em>",
    "subtitle": "환자·보호자의 일상을 의료진의 질문에 연결하는 AI 소통 솔루션",
    "note": "EONU IR · 기획 개선본 · 2026.10.21",
    "talk": "안녕하세요. 이어지는 진료, 세 사람의 안심을 만드는 이어온유입니다. 환자와 보호자의 일상을 의료진의 질문에 연결하고, 진료 후 계획을 다시 일상으로 잇고자 합니다."
  },
  {
    "id": "02",
    "section": "PROBLEM",
    "title": "혼자 병원에 와도, <em>필요한 이야기는 함께 와야 합니다</em>",
    "subtitle": "동행하지 못한 보호자의 관찰과 환자의 경험이 진료실까지 이어지지 않는 순간",
    "note": "재구성한 설명용 사례. TV조선 2023.07.26 보도는 단독 내원 논란의 맥락 자료이며, 소통 공백의 빈도·증가를 입증하지 않습니다.",
    "talk": "아이가 혼자 병원에 왔습니다. 언제부터 어떤 변화가 있었는지 정확히 설명하기 어렵고, 관찰을 알고 있는 보호자는 곁에 없습니다. 의료진도 필요한 정보를 짧은 시간 안에 파악해야 합니다. 이 장면은 설명을 위해 재구성한 사례입니다. 우리가 풀려는 문제는 동행의 부재가 만드는 정보 전달의 공백입니다."
  },
  {
    "id": "03",
    "section": "THREE-SIDED VALUE",
    "title": "서로 다른 필요를 <em>하나의 소통 흐름으로</em>",
    "subtitle": "환자의 경험, 보호자의 관찰, 의료진의 질문과 안내를 역할에 맞게 연결합니다.",
    "note": "제품이 지향하는 가치와 연결 구조. 임상 효과·업무 시간 절감이 검증되었다는 의미는 아닙니다.",
    "talk": "환자는 자신의 상황을 이해받고 싶고, 보호자는 관찰을 전달하고 진료 후 도울 일을 알고 싶습니다. 의료진은 필요한 정보를 빠르게 확인해야 합니다. 이어온유는 일상의 이야기를 병원이 요청한 정보로 정리하고, 역할과 공유 범위에 맞게 전달합니다. 진료에서 확인한 계획을 다시 일상으로 이어주는 구조입니다."
  },
  {
    "id": "04",
    "section": "ADOPTION HYPOTHESIS",
    "title": "환자의 걱정이 병원의 <em>상담 기회로 이어진다면?</em>",
    "subtitle": "병원 도입을 설명하는 세 가지 가치 중, 초기에는 수익 기여 가능성을 검증합니다.",
    "note": "검증할 사업 가설. 개별 비급여의 필요성·상담 전환 성과는 미입증. 정보 제공·상담 연결 방식은 법적 검토 범위를 확인해야 합니다.",
    "talk": "가족에게 필요한 연결이어도, 병원에 확인 업무만 늘어난다면 지속되기 어렵습니다. 도입 가치는 진료 효율, 임상적 유용성, 수익 기여로 나눠 보겠습니다. 초기에는 미해결 걱정을 구체화하고 병원의 관련 정보를 알려주는 것이 자발적인 상담으로 이어질지 검증합니다. 비급여 필요성을 AI가 판단하는 구조는 아닙니다. 환자의 상담 요청과 병원의 지불 의사뿐 아니라 전체 업무 부담을 함께 측정하겠습니다."
  },
  {
    "id": "05",
    "section": "SOLUTION · 01",
    "title": "<em>병원의 기준</em>으로 시작하는 소통",
    "subtitle": "① 의료진 → EONU: 먼저 확인할 질문, 서비스 정보, 진료 후 안내를 설정합니다.",
    "note": "설명용 제품 구조. 병원 안내 QR은 진입 방식이며, 이 자료에는 실제 접속용 QR을 넣지 않았습니다.",
    "talk": "출발점은 의료진의 참여입니다. 병원이 확인할 질문, 안내할 서비스 정보, 진료 후 관리 내용을 먼저 설정합니다. 환자와 보호자는 병원이 안내한 QR 등으로 연결 화면에 들어옵니다. 기존 광고와 환자관리도 존재합니다. 이어온유는 병원의 질문에 환자와 가족의 관찰을 맞추고, 직접 확인한 내용을 다음 진료까지 잇는 방식의 가치를 검증하려 합니다."
  },
  {
    "id": "06",
    "section": "DEMO FLOW",
    "title": "편하게 기록하고, <em>전달할 내용은 직접 확인합니다</em>",
    "subtitle": "병원 설정 → 환자·보호자 기록 → 전달 전 확인 → 의료진 확인",
    "note": "실제 서비스 캡처가 아닌 설명용 UI 도식·가상 데이터. 구현 완료나 안전성 검증, EMR 연동 완료를 의미하지 않습니다.",
    "talk": "병원이 질문과 안내를 설정하면 환자와 보호자는 달력에서 할 일을 확인하고, 일기나 음성, 체크로 기록합니다. AI는 전달 요약 초안을 정리합니다. 당사자는 원문과 요약을 비교하고 공유할 항목과 범위를 조정합니다. 의료진은 작성자와 확인 상태를 구분해 보고, 진료 후 안내를 다시 전달합니다. 지금 보시는 화면은 이 흐름을 설명하기 위한 도식입니다."
  },
  {
    "id": "07",
    "section": "BUSINESS MODEL",
    "title": "병원에서 시작하고, <em>공공 영역도 검증합니다</em>",
    "subtitle": "초기 B2B 라이선스 → 유료 도입 검증 → B2B2C 확장 · B2G는 별도 구매 경로",
    "note": "첫 병원군·가격·계약 상태 미확정. B2G는 공공 구매 계약을 의미하며, 연구지원금·민간 봉사활동과 구분합니다.",
    "talk": "초기 고객은 일차의료기관이며 B2B 라이선스를 가정합니다. 첫 병원군은 반복되는 소통 문제와 도입 가치, 실증 가능성으로 좁히겠습니다. 가상 사례 검토, 제한 실증, 유료 제안과 계약을 구분해 진행합니다. 이후 환자·보호자의 추가 유료 가치를 검토하고, 공공 영역은 실제 구매기관과 예산이 있는 별도 경로로 검증하겠습니다."
  },
  {
    "id": "08",
    "section": "MARKET LOGIC",
    "title": "<em>현재 판매할 상품</em>으로 시장을 계산합니다",
    "subtitle": "소프트웨어 매출 기준 · 시장의 상한과 일정 기간 내 실제 확보 목표를 분리",
    "note": "원문의 시장 입력값은 미확정. 포함 관계를 나타낸 개념도이며 도형 면적은 시장 금액·비율에 비례하지 않습니다.",
    "talk": "시장 규모는 지금 판매하려는 소프트웨어를 기준으로 계산하겠습니다. 적용 가능한 전체 범위, 초기 고객 조건에 맞는 시장, 일정 기간 내 실제 확보 목표를 구분합니다. 기관 수와 연간 가격은 아직 확정 전입니다. B2B2C와 B2G도 각 구매 단위로 계산하되 동일 계약과 중복 합산하지 않습니다. 미래 하드웨어 매출과 연구지원금은 제외하겠습니다."
  },
  {
    "id": "09",
    "section": "SCALE-UP · 02",
    "title": "쌓이는 일상 정보를 <em>진료에 활용하도록</em>",
    "subtitle": "② 환자 → EONU: 병원 도입 검증 이후, 정보의 임상적 유용성과 수집 부담을 확인합니다.",
    "note": "확장 방향·연구 과제. EMR·외부 앱·기기 연동 및 디지털 바이오마커는 구현·임상 검증 완료를 의미하지 않습니다.",
    "talk": "의료진의 도입이 검증된 후에는 환자의 일상 정보가 진료에 얼마나 쓰이는지 살펴보겠습니다. 입력 부담과 반복 사용도 함께 봅니다. EMR과 외부 건강 앱 연결은 권한과 연동 비용을 확인해야 합니다. ADHD나 노년층에서의 기기 연동과 디지털 바이오마커는 대상별 접근성과 임상적 의미를 검토할 추가 연구 과제입니다."
  },
  {
    "id": "10",
    "section": "PROGRESS & VALIDATION",
    "title": "현장에서 쓰이는 <em>연결 방식을 축적합니다</em>",
    "subtitle": "진행 상태를 구분하고, 다음 검증에서 실제 활용·업무 부담·지불 의사를 확인합니다.",
    "note": "2026.10.20 MD 기재 기준. 기관·전문의 관련 언급은 자문·협의 범위 확인 필요. 계약·실증 실적 또는 공식 제휴로 표시하지 않았습니다.",
    "talk": "현재 자료에는 전문의의 지속적인 피드백과 기관 접점, 청년 우울증 관련 봉사 프로젝트 참여가 기재되어 있습니다. 이들을 실증이나 유료 계약 실적으로 합치지는 않았습니다. MVP 범위와 각 협력의 실제 상태는 증빙에 맞춰 확정하겠습니다. 다음에는 의료진의 실제 활용, 전체 업무 부담, 반복 사용과 구매 의사를 확인해 질문과 템플릿, 운영 경험을 축적하겠습니다."
  },
  {
    "id": "11",
    "section": "TEAM & CAPITAL PLAN",
    "title": "<em>1억 원</em>으로 첫 유료 모델을 검증하겠습니다",
    "subtitle": "직접 기획·개발하는 실행력을 바탕으로, 제품과 실증·고객 확보를 연결합니다.",
    "note": "1억 원은 MD의 사용계획 총액. 항목별 배분·집행 기간·실증 및 유료 고객 목표·CAC는 미확정이며 [ ]로 유지했습니다.",
    "talk": "저는 의료와 AI에 대한 이해를 바탕으로 기획과 개발, 수정을 직접 이어갑니다. 임상 확인과 개인정보·보안, 실증 운영을 함께할 협력이 필요합니다. 1억 원은 제품, 보안, 실증, 고객 확보와 운영에 연결해 사용할 계획입니다. 항목별 배분과 기간, 실증 기관 수, 유료 고객 목표를 확정하고 고객 획득 비용까지 계산하겠습니다. 소개와 직접 접촉, 방문 데모와 파일럿으로 첫 유료 모델을 검증하겠습니다."
  },
  {
    "id": "12",
    "section": "CLOSING",
    "title": "환자·보호자가 원하는 연결, <em>의료진도 지속할 이유</em>",
    "subtitle": "일상의 이야기를 진료로, 진료의 계획을 일상으로.",
    "note": "EONU · 이어온유 · IR 기획 개선본",
    "talk": "이어온유는 환자와 보호자가 원하는 연결을, 의료진도 지속적으로 참여할 이유가 있는 서비스로 만들겠습니다. 첫 병원군과 함께 실제로 쓰이고 지불할 가치가 있는지 검증하겠습니다. 감사합니다."
  }
];
(function(){
 const E=window.EONU,{ph,tag,icon,arrow,relation}=E,S=E.slides;
 const set=(n,meta,content)=>Object.assign(S[n-1],meta,{content});
 set(1,{title:'이어지는 진료, 세 사람의 안심',section:''},`
  ${ph('환자 · 보호자 · 의료진의 일상 장면','cover-image')}
  <div class="cover-mark">EONU<span>이어온유 · AI 소통 솔루션</span></div>
  <h1 class="cover-title">이어지는 진료,<br><em>세 사람의 안심.</em></h1>
  <div class="cover-word">EONU</div>
  <p class="cover-sub">일상의 이야기를 진료로,<br>진료의 계획을 일상으로.</p>
  <div class="cover-foot">INVESTOR PRESENTATION · 2026.10</div>
  <div class="cover-connect"><div class="cover-person">${icon('person')}환자</div>${arrow()}<div class="cover-person">${icon('doctor')}의료진</div>${arrow()}<div class="cover-person">${icon('family')}보호자</div></div>`);
 set(2,{section:'문제 인식',title:'혼자 온 진료실에, <em>함께 와야 할 이야기</em>',subtitle:'동행의 부재가 만드는 정보 전달의 공백에서 시작합니다.'},`
  <div class="storyboard">${[
   ['01 · 환자','아이의 진료 장면','“언제부터 그랬나요?”','변화의 시점과 상태를<br>정확히 설명하기 어렵습니다.'],
   ['02 · 보호자','동행하지 못한 보호자','“전할 말이 있는데”','관찰한 내용은 있지만<br>지금 곁에 있을 수 없습니다.'],
   ['03 · 의료진','진료 중 정보를 확인하는 의료진','“확인할 정보가 필요해요”','제한된 시간 안에<br>필요한 내용을 파악해야 합니다.'],
   ['04 · EONU','함께 전달한 내용을 보는 장면','“함께 남긴 내용을 확인”','환자·보호자가 선택한 정보를<br>의료진에게 연결합니다.']
  ].map(a=>`<div class="story">${ph(a[1])}<div class="story-index">${a[0]}</div><h3>${a[2]}</h3><p>${a[3]}</p></div>`).join('')}</div>
  <div class="story-summary"><b>필요한 이야기도, 환자와 함께 진료실에 도착해야 합니다.</b><span>재구성한 설명용 사례</span></div>`);
 set(3,{section:'세 사람의 필요',title:'서로 다른 필요를 <em>하나의 소통 흐름으로</em>',subtitle:'환자의 경험, 보호자의 관찰, 의료진의 질문과 안내를 역할에 맞게 연결합니다.'},`
  <div class="positioned p03-relation">${relation()}</div>
  <div class="needs"><div class="need"><h3>환자 · 내 상황을 알아주길</h3><p>일상 경험과 걱정을<br>필요한 내용으로 전달합니다.</p></div><div class="need"><h3>보호자 · 전달하고 돕고 싶음</h3><p>관찰을 공유하고<br>진료 후 도울 일을 확인합니다.</p></div><div class="need"><h3>의료진 · 빠르게 파악하고 싶음</h3><p>병원이 요청한 정보와<br>원문을 함께 확인합니다.</p></div></div>
  <div class="cycle-line">${icon('link')}확인된 계획이 다시 일상으로</div>`);
 set(4,{section:'병원 도입 가설',title:'환자의 걱정이<br><em>병원의 상담 기회로</em>',subtitle:'의료진이 지속해서 참여할 이유.<br>초기에는 수익 기여 가능성을 검증합니다.'},`
  ${ph('의료진이 환자의 걱정을 듣는 상담 장면','adoption-image')}
  <div class="adoption-values"><div class="value-item"><strong>진료 효율</strong><span>전체 업무 부담 측정</span></div><div class="value-item"><strong>임상적 유용성</strong><span>실제 활용 여부 확인</span></div><div class="value-item active"><strong>수익 기여</strong><span>초기 검증 초점</span></div></div>
  <div class="adoption-flow"><div><span class="step-no">01 / 미해결 걱정</span><h3>일상에서 구체화</h3><p>환자·보호자의 기록과 질문으로<br>관심과 궁금증을 확인합니다.</p></div>${arrow()}<div><span class="step-no">02 / 관련 정보</span><h3>병원의 안내와 연결</h3><p>병원이 설정한 서비스 정보를<br>환자가 확인합니다.</p></div>${arrow()}<div><span class="step-no">03 / 자발적 상담</span><h3>환자가 상담을 선택</h3><p>의료진이 필요성을 판단하고<br>지불할 업무 가치를 검증합니다.</p></div></div>
  <p class="adoption-proof">홈페이지·SNS·광고와 병행 · 측정: 정보 확인 → 상담 요청 → 병원의 유료 도입 의사</p>`);
 set(5,{section:'솔루션 구조 ①',title:'<em>병원의 기준</em>으로 시작하는 소통',subtitle:'의료진이 확인할 질문, 서비스 정보, 진료 후 안내를 먼저 설정합니다.'},`
  ${ph('질문과 서비스 정보를 설정하는 의료진','solution-image')}
  <p class="solution-caption">의료진의 질문이<br>일상 기록의 기준이 됩니다.</p>
  <div class="positioned p05-relation">${relation('doctor')}</div>
  <div class="setup-strip">${icon('link')}병원 안내 QR → 환자·보호자 연결 화면에서 시작</div>`);
 set(6,{section:'데모 진행 흐름',title:'편하게 기록하고, <em>전달 전 직접 확인합니다</em>',subtitle:'병원 설정 → 환자·보호자 기록 → 공유 범위 확인 → 의료진 확인'},`
  <div class="demo-flow">
   <div class="demo-step"><div class="demo-heading"><b>01</b><h3>의료진 세팅</h3></div><div class="demo-panel"><div class="screen-label">병원이 정하는 확인 기준</div><div class="ui-field selected">질문: 변화가 시작된 시점</div><div class="ui-field">질문: 불편했던 일상 장면</div><div class="ui-field">서비스 정보와 관리 안내</div><div class="screen-label">질문 · 관련 정보 · 진료 후 할 일</div><div class="ui-action">환자·보호자에게 안내</div></div></div>
   <div class="demo-step"><div class="demo-heading"><b>02</b><h3>일상 기록</h3></div><div class="demo-panel"><div class="screen-label">달력에서 할 일 확인</div><div class="ui-week">${['월','화','수','목','금','토','일','12','13','14','15','16','17','18'].map(t=>`<span class="${t==='14'?'selected':''}">${t}</span>`).join('')}</div><div class="ui-field">✓ 오늘의 관리 계획 확인</div><div class="ui-field">일기 · 음성 · 체크로 기록</div><div class="ui-tags"><span>환자 기록</span><span>보호자 관찰</span></div><div class="ui-action">AI가 전달 요약 초안 정리</div></div></div>
   <div class="demo-step"><div class="demo-heading"><b>03</b><h3>공유 전 확인</h3></div><div class="demo-panel"><div class="screen-label">원문과 요약을 함께 확인</div><div class="ui-field selected">원문 “저녁에 더 불편했어요.”</div><div class="ui-field">요약: 저녁 불편감 보고<small>시작 시점: 미확인</small></div><div class="ui-toggle-row"><span>이 항목 공유</span><span class="ui-toggle"></span></div><div class="ui-toggle-row"><span>공유 대상</span><span>담당 병원</span></div><div class="ui-action">당사자 확인 후 전달</div></div></div>
   <div class="demo-step"><div class="demo-heading"><b>04</b><h3>의료진 확인</h3></div><div class="demo-panel"><div class="screen-label">요청 항목별 전달 내용</div><div class="ui-field selected">요약 + 연결된 원문 확인</div><div class="ui-field">환자 / 보호자 작성 구분</div><div class="ui-field">미확인 항목은 추가 질문</div><div class="screen-label">확인 상태 구분 · 기존 EMR 옆 화면</div><div class="ui-action">진료 후 안내 → 일상으로</div></div></div>
  <span class="demo-next next-1">${icon('arrow')}</span><span class="demo-next next-2">${icon('arrow')}</span><span class="demo-next next-3">${icon('arrow')}</span></div><p class="demo-proof">원문 · 작성자 · 시점 · 확인 상태를 남기고, 공유 범위를 직접 조정합니다.</p>`);
 set(7,{section:'사업 모델',title:'병원에서 시작하고, <em>공공 영역도 검증합니다</em>',subtitle:'초기 B2B 라이선스에서 유료 도입을 검증한 뒤 확장합니다.'},`
  ${ph('첫 실증과 도입을 논의하는 병원 현장','bm-image')}
  <div class="bm-side"><h3>첫 고객은<br>일차의료기관</h3><p>반복되는 소통 문제 × 도입 가치<br>× 실증 협조 가능성으로 선정</p></div>
  <div class="bm-model"><div class="bm-primary"><div><h3>B2B 라이선스</h3><p>기관 단위 반복 이용료 가설</p></div><span>먼저 검증할<br><b>핵심 매출 경로</b></span></div><div class="bm-branches"><div class="bm-branch"><h3>B2B2C</h3><p>환자·보호자의 추가 유료 가치<br>병원 도입 이후 별도 검증</p></div><div class="bm-branch"><h3>B2G</h3><p>소통 지원이 필요한 현장<br>구매기관·예산·조달 경로 확인</p></div></div></div>
  <div class="bm-gates"><strong>가상 사례 검토 → 제한 실증 → 유료 제안 → 계약</strong><p>동의·공유 권한·의료진 확인 절차와 전체 업무 부담을 함께 점검</p></div>`);
 set(8,{section:'시장 산정',title:'<em>현재 판매할 상품</em>으로 시장을 계산합니다',subtitle:'소프트웨어의 매출 상한과 일정 기간 내 실제 확보 목표를 구분합니다.'},`
  <div class="market-visual" role="img" aria-label="TAM 전체 적용 시장 안에 SAM 초기 집중시장, 그 안에 SOM 기간 내 확보 목표가 포함됩니다. 면적은 금액에 비례하지 않습니다."><svg viewBox="0 0 512 384"><circle class="ring-outer" cx="256" cy="192" r="184"/><circle class="ring-middle" cx="256" cy="224" r="136"/><circle class="ring-inner" cx="256" cy="256" r="88"/><text x="256" y="52" text-anchor="middle" font-size="28">TAM</text><text x="256" y="76" text-anchor="middle" font-size="14">적용 가능한 전체 소프트웨어 시장</text><text x="256" y="128" text-anchor="middle" font-size="28">SAM</text><text x="256" y="152" text-anchor="middle" font-size="14">초기 집중시장</text><text class="inverse" x="256" y="252" text-anchor="middle" font-size="36">SOM</text><text class="inverse" x="256" y="284" text-anchor="middle" font-size="14">기간 내 유료 고객 목표</text></svg></div>
  <p class="market-caption">포함 관계를 나타낸 개념도 · 금액·비율에 비례하지 않음</p>
  <div class="market-formulas"><div class="formula-row"><h3>B2B · 기관 라이선스</h3><div class="formula">대상 기관 <span>[ ]곳</span> × 연간 가격 <span>[ ]원</span></div><p>초기 시장 상한과 실제 유료 고객 목표를 분리</p></div><div class="formula-row"><h3>B2B2C · 추가 유료 서비스</h3><div class="formula">이용자 × 유료 전환율 × 연간 이용액</div><p>기관 계약에 포함된 요금과 중복 합산하지 않음</p></div><div class="formula-row"><h3>B2G · 별도 구매 계약</h3><div class="formula">구매사업 <span>[ ]건</span> × 계약 단가 <span>[ ]원</span></div><p>동일 공급 계약·연구지원금·미래 기기 매출 제외</p></div></div>
  <p class="market-price">가격은 제공 원가·운영 비용과 업무 가치·지불 의사로 검증</p>`);
 set(9,{section:'스케일업 ②',title:'쌓이는 일상 정보를 <em>진료에 활용하도록</em>',subtitle:'병원 도입 검증 이후, 환자 정보의 임상적 유용성과 수집 부담을 확인합니다.'},`
  ${ph('일상을 기록하는 환자와 가족 · 기기 활용 장면','scale-image')}
  <p class="scale-caption">정보의 의미와<br>입력 부담을 함께 검증합니다.</p>
  <div class="positioned p09-relation">${relation('patient')}</div>
  <div class="scale-road"><div><b>01</b>일상 기록의 활용·반복 사용</div><div><b>02</b>EMR·외부 앱 연동 검토</div><div><b>03</b>기기·바이오마커 추가 연구</div></div>`);
 set(10,{section:'현재 진척과 검증',title:'진척은 <em>증빙</em>으로, 다음 단계는 <em>지표</em>로',subtitle:'현장에서 실제로 쓰이는 질문·정보 구조·운영 경험을 축적합니다.'},`
  ${ph('현장 인터뷰 · 피드백을 반영하는 제품 검토','progress-image')}
  <div class="progress-side"><h3>다음 검증의 초점은<br>사용 · 부담 · 구매</h3><div class="progress-metrics"><span><b>01</b>의료진 확인율 · 정보 수정·누락</span><span><b>02</b>작성·확인·후속 업무의 전체 부담</span><span><b>03</b>반복 사용 · 유료 제안 · 계약</span></div></div>
  <div class="status-table"><div class="status-head"><span>확인 항목</span><span>최신 MD 기재 내용</span><span>자료 상태</span></div>${[
   ['MVP','구현 범위·사용 가능 기능 [확인 필요]','미확정'],
   ['전문의 피드백','정신과 전문의의 지속 피드백 언급','범위 확인'],
   ['기관 접점','의료혁신 연구소 관련 접점 언급','상태 확인'],
   ['봉사 프로젝트','청년 우울증·자선사업 참여 확정 기재','원문 기재'],
   ['실증 · 유료 계약','기관 수·기간·계약 증빙 [확인 필요]','미확정'],
   ['법적 검토','검토 범위·의견·완료일 [확인 필요]','미확정']
  ].map(r=>`<div class="status-row"><b>${r[0]}</b><span class="detail">${r[1]}</span>${tag(r[2],r[2]==='원문 기재'?'':'neutral')}</div>`).join('')}</div>
  <p class="progress-asset">축적 자산: 질문 · 템플릿 · 피드백 반영 · 운영 경험</p>`);
 set(11,{section:'팀과 자금 사용계획',title:'<em>1억 원</em>으로 첫 유료 모델을 검증합니다',subtitle:'직접 기획·개발하는 실행력에 임상 확인·보안·실증 운영 협력을 더합니다.'},`
  ${ph('대표 인물 사진','founder-image')}
  <div class="founder-copy"><h3>기획 → 개발 → 수정</h3><p>의료·AI 이해를 바탕으로<br>현장 질문을 제품으로 구현하고<br>피드백을 직접 반영합니다.</p></div>
  <div class="budget"><div class="budget-total">1억<span>원</span></div><div class="eyebrow">USE OF FUNDS · 배분 확정 전</div>${['제품 개발·개선','개인정보·보안 검토','실증 설계·운영','고객 확보·방문 데모','API·클라우드·운영'].map(t=>`<div class="budget-line"><span>${t}</span><span>[ ]만 원</span></div>`).join('')}<div class="budget-caption">항목별 합계 = 10,000만 원<br>제공 원가와 고객 획득 비용은 분리 산정</div></div>
  <div class="capital-outcomes"><h3>자금이 만들 검증 결과</h3><div class="capital-step"><strong>[ ]개월</strong><div><b>집행 기간</b><p>월별 소진 계획과 연결</p></div></div><div class="capital-step"><strong>[ ]곳</strong><div><b>실증 기관</b><p>활용·부담·반복 사용 확인</p></div></div><div class="capital-step"><strong>[ ]곳</strong><div><b>유료 고객</b><p>가격 수용성과 구매 검증</p></div></div><div class="capital-acquisition">소개·접촉 → 방문 데모 → 파일럿 → 유료 제안<br>CAC = 획득 비용 ÷ 신규 유료 기관 수</div></div>`);
 set(12,{title:'환자·보호자가 원하는 연결, 의료진도 지속할 이유',section:''},`
  ${ph('일상으로 돌아온 환자와 보호자의 장면','closing-image')}
  <div class="closing-mark">EONU</div>
  <h1 class="closing-title">환자·보호자가 원하는 연결,<br><em>의료진도 지속할 이유.</em></h1>
  <p class="closing-sub">첫 병원군과 함께,<br>현장에서 쓰이고 지불할 가치를 검증하겠습니다.</p>
  <div class="closing-relation">${relation('all',true)}</div>
  <div class="closing-sentence">일상의 이야기를 진료로,<br>진료의 계획을 일상으로.</div>
  <div class="closing-contact">이어온유 · 연락처 [확인 후 입력]</div>`);
})();
