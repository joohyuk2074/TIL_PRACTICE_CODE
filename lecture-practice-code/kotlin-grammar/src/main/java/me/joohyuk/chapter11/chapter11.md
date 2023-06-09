# Chapter 11. 코틀린에서 접근 제어를 다루는 방법
- Kotlin에서 패키지는 namespace 관리용이기 때문에 protected는 의미가달라졌다.
- Kotlin에서는 default가 사라지고, 모듈간의 접근을 통제하는 internal이 새로 생겼다.
- 생성자에 접근 지시어를 붙일 때는 constructor를 명시적으로 써주어야 한다.
- 유틸성 함수를 만들 때는 파일 최상단을 이용하면 편리하다.
- 프로퍼티의 custom setter에 접근 지시어를 붙일 수 있다.
- Java에서 Kotlin 코드를 사용할 때 internal과 protected는 주의해야 한다.