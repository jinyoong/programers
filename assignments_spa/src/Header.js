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
    const urlChange = new CustomEvent('urlchange', {
      detail: { href: url }
    });
    document.dispatchEvent(urlChange)
  }

  render() {
    const header = document.createElement('header');
    const homeMenu = this.makeHeaderMenu('header header_left', 'menu_home', 'menu_name', 'HOME')
    homeMenu.addEventListener('click', () => this.changeUrl('/assignments_spa/'))
    // 경로를 해설에서의 /web/ 이 아닌 /assignments_spa/ 로 한 이유는 live server로 열었을 때의 기본 경로가 최상단 폴더이기 때문!

    const signupMenu = this.makeHeaderMenu('header header_right', 'menu_signup', 'menu_name', 'SIGNUP')
    signupMenu.addEventListener('click', () => this.changeUrl('/assignments_spa/signup'))

    header.appendChild(homeMenu);
    header.appendChild(signupMenu);
    this.$body.appendChild(header);
  }
}

export default Header;