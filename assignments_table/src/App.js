import Table from "./Table.js";
import Pagination from "./Pagination.js";

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
        console.log("불러온 데이터 : ", tableData);
        new Table(tableData, 0, 4);
        new Pagination(1, 5);
      };
    } catch (error) {
      console.log(error)
    }
  };
};

export default App;