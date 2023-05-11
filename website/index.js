//import { getData, parser } from "./get_data.js";

/*
//top level domain testing: works
let date = ["10/06/2023", "12/06/2023", "13/06/2023", "14/06/2023", "15/06/2023", "16/06/2023", "17/06/2023", "18/06/2023", "19/06/2023", "20/06/2023", "21/06/2023", "22/06/2023", "23/06/2023", "24/06/2023"]
date.forEach((key) => {
  getData(key).then((data) => {
   console.log(parser(data));
  });
});
*/

import { button_handler } from "./html_generator.js"; //{ for named exports } no brackets for default exports
button_handler("10/06/2023");