class Signup {
  constructor($body) {
    this.$body = $body;
  }

  render() {
    const main = document.createElement('main');
    main.setAttribute('id', 'page_content');
    main.textContent = "회원가입 페이지 렌더";
    this.$body.appendChild(main);
  }
}

export default Signup;