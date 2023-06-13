class Home {
  constructor($body) {
    this.$body = $body;
  }

  render() {
    const main = document.createElement('main');
    main.setAttribute('id', 'page_content');
    main.textContent = "메인페이지 렌더";
    this.$body.appendChild(main);
  }
}

export default Home;