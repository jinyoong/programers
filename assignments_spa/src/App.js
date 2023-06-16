import Header from './Header.js';
import Home from './Home.js';
import Signup from './Signup.js';
import setPersonalInfo from './Storage.js';

class App {
  constructor($body) {
    this.$body = $body;
    this.render();
  }

  async render() {
    const header = new Header(this.$body);
    header.render();

    const home = new Home(this.$body);
    const signup = new Signup(this.$body);

    home.render();

    await setPersonalInfo();

    document.addEventListener('urlchange', (event) => {
      let pathname = event.detail.href;
      console.log(pathname);

      switch (pathname) {
        case '/assignments_spa/':
          home.render();
          break;
        case '/assignments_spa/signup':
          signup.render();
          break;
        default:
      }
    })
  }
}

export default App