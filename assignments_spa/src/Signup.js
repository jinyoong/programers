class Signup {
  constructor($body) {
    this.$body = $body;
  }

  render() {
    const main = document.createElement('main');
    main.setAttribute('id', 'page_content');
    this.$body.appendChild(main);
  }
}

export default Signup;