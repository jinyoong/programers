import Header from './Header.js';
import Home from './Home.js';

class App {
  constructor($body) {
    this.$body = $body;
    this.render();
  }

  render() {
    const header = new Header(this.$body);
    header.render();

    const home = new Home(this.$body);
    home.render();
  }
}

export default App