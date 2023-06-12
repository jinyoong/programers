class Header {
  constructor($body) {
    this.$body = $body;
  }

  makeHeaderMenu(divClass, spanId, spanClass, spanText) {
    const div = document.createElement('div');
    div.className = divClass;

    const span = document.createElement('span');
    span.setAttribute('id', spanId);
    span.setAttribute('class', spanClass);
    span.textContent = spanText;

    div.appendChild(span);
    return div;
  }

  changeUrl(url) {
    window.history.pushState('', '', url);
  }

  render() {
    const header = document.createElement('header');
    const homeMenu = this.makeHeaderMenu('header header_left', 'menu_home', 'menu_name', 'HOME')
    homeMenu.addEventListener('click', () => this.changeUrl('/web/'))

    const signupMenu = this.makeHeaderMenu('header header_right', 'menu_signup', 'menu_name', 'SIGNUP')
    signupMenu.addEventListener('click', () => this.changeUrl('/web/signup/'))

    header.appendChild(homeMenu);
    header.appendChild(signupMenu);
    this.$body.appendChild(header);
  }
}

export default Header;