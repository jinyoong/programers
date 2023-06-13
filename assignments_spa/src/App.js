import Header from './Header.js';
import Home from './Home.js';
import Signup from './Signup.js';

class App {
  constructor($body) {
    this.$body = $body;
    this.render();
  }

  render() {
    const header = new Header(this.$body);
    header.render();

    const home = new Home(this.$body);
    const signup = new Signup(this.$body);

    home.render();

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