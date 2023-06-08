import Table from "./Table.js";

class App {
  constructor($app) {
    this.$app = $app;
    this.render();
  };

  async render() {
    try {
      const response = await fetch("./src/data.json");
      
      if (response.ok) {
        const tableData = await response.json();
        const options = [4, 8];
        console.log("불러온 데이터 : ", tableData);
        new Table(tableData);
      };
    } catch (error) {
      console.log(error)
    }
  };
};

export default App;