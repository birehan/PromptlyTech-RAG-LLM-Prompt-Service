// import { useEffect, useState } from 'react';
// import Plot from 'react-plotly.js';
// import axios from 'axios';


// const Home = () => {
//   const [data, setData] = useState([]);

//   useEffect(() => {
//      getData()
//   }, []);

//   const getData = async() => {
//   try{
//     const response = await axios.post('http://127.0.0.1:5000/api/v1/chat', {"question": ""});
//     setData(JSON.parse(response.data))
//     return JSON.parse(response.data);
//   }    
//   catch(e){
//     setData("error: ", e);
//   }
//   }
//   console.log("data: ", data)

//   return (
//     <div>
//       <h2>Data Visualization</h2>
//       <Plot
//         data={[
//           {
//             x: Object.keys(data), // Assuming your DataFrame columns are the x-axis
//             y: Object.values(data), // Values corresponding to each column
//             type: 'bar',
//             marker: { color: 'blue' },
//           },
//         ]}
//         layout={{ width: 800, height: 400, title: 'DataFrame Columns Visualization' }}
//       />
//     </div>
//   );
// };

// export default Home;


import { useState, useEffect } from 'react';
import axios from 'axios';

const YourComponent = () => {
  const [data, setData] = useState(null);

  const text =  "{\"question\":{\"0\":\"What project did OpenAI use to showcase the capabilities of reinforcement learning algorithms?\",\"1\":\"When was OpenAI founded?\",\"2\":\"What is the goal of OpenAI?\",\"3\":\"What toolkit did OpenAI release in 2016?\",\"4\":\"What game did the AI agents trained by OpenAI play?\"},\"answer\":{\"0\":\"OpenAI used the 'OpenAI Five' project to showcase the capabilities of reinforcement learning algorithms.\",\"1\":\"OpenAI was founded in 2015.\",\"2\":\"The goal of OpenAI is to advance digital intelligence in a way that benefits humanity as a whole.\",\"3\":\"OpenAI released the 'OpenAI Gym' toolkit in 2016.\",\"4\":\"The AI agents trained by OpenAI played a game called 'Dota 2'.\"},\"contexts\":{\"0\":[\"OpenAI showcased the capabilities of these reinforcement learning algorithms through its \\u2018OpenAI Five\\u2019 \\nproject in 2018, which trained five independent AI agents to play a complex multiplayer online battle \\narena game called \\u2018Dota 2\\u2019. Despite operating independently, these agents learned to work as a cohesive \\nteam to coordinate strategies within the game.\",\"The early years of OpenAI were marked with rapid experimentation. The company made significant progress \\non research in deep learning and reinforcement learning, and released \\u2018OpenAI Gym\\u2019 in 2016, a toolkit \\nfor developing and comparing reinforcement learning algorithms.\",\"OpenAI was initially founded in 2015 by Sam Altman, Elon Musk, Ilya Sutskever and Greg Brockman as a \\nnon-profit organization with the stated goal to \\u201cadvance digital intelligence in the way that is most \\nlikely to benefit humanity as a whole.\\u201d The company assembled a team of the best researchers in the \\nfield of AI to pursue the goal of building AGI in a safe way.\"],\"1\":[\"The early years of OpenAI were marked with rapid experimentation. The company made significant progress \\non research in deep learning and reinforcement learning, and released \\u2018OpenAI Gym\\u2019 in 2016, a toolkit \\nfor developing and comparing reinforcement learning algorithms.\",\"OpenAI was initially founded in 2015 by Sam Altman, Elon Musk, Ilya Sutskever and Greg Brockman as a \\nnon-profit organization with the stated goal to \\u201cadvance digital intelligence in the way that is most \\nlikely to benefit humanity as a whole.\\u201d The company assembled a team of the best researchers in the \\nfield of AI to pursue the goal of building AGI in a safe way.\",\"OpenAI showcased the capabilities of these reinforcement learning algorithms through its \\u2018OpenAI Five\\u2019 \\nproject in 2018, which trained five independent AI agents to play a complex multiplayer online battle \\narena game called \\u2018Dota 2\\u2019. Despite operating independently, these agents learned to work as a cohesive \\nteam to coordinate strategies within the game.\"],\"2\":[\"OpenAI was initially founded in 2015 by Sam Altman, Elon Musk, Ilya Sutskever and Greg Brockman as a \\nnon-profit organization with the stated goal to \\u201cadvance digital intelligence in the way that is most \\nlikely to benefit humanity as a whole.\\u201d The company assembled a team of the best researchers in the \\nfield of AI to pursue the goal of building AGI in a safe way.\",\"The early years of OpenAI were marked with rapid experimentation. The company made significant progress \\non research in deep learning and reinforcement learning, and released \\u2018OpenAI Gym\\u2019 in 2016, a toolkit \\nfor developing and comparing reinforcement learning algorithms.\",\"OpenAI showcased the capabilities of these reinforcement learning algorithms through its \\u2018OpenAI Five\\u2019 \\nproject in 2018, which trained five independent AI agents to play a complex multiplayer online battle \\narena game called \\u2018Dota 2\\u2019. Despite operating independently, these agents learned to work as a cohesive \\nteam to coordinate strategies within the game.\"],\"3\":[\"The early years of OpenAI were marked with rapid experimentation. The company made significant progress \\non research in deep learning and reinforcement learning, and released \\u2018OpenAI Gym\\u2019 in 2016, a toolkit \\nfor developing and comparing reinforcement learning algorithms.\",\"OpenAI showcased the capabilities of these reinforcement learning algorithms through its \\u2018OpenAI Five\\u2019 \\nproject in 2018, which trained five independent AI agents to play a complex multiplayer online battle \\narena game called \\u2018Dota 2\\u2019. Despite operating independently, these agents learned to work as a cohesive \\nteam to coordinate strategies within the game.\",\"OpenAI was initially founded in 2015 by Sam Altman, Elon Musk, Ilya Sutskever and Greg Brockman as a \\nnon-profit organization with the stated goal to \\u201cadvance digital intelligence in the way that is most \\nlikely to benefit humanity as a whole.\\u201d The company assembled a team of the best researchers in the \\nfield of AI to pursue the goal of building AGI in a safe way.\"],\"4\":[\"OpenAI showcased the capabilities of these reinforcement learning algorithms through its \\u2018OpenAI Five\\u2019 \\nproject in 2018, which trained five independent AI agents to play a complex multiplayer online battle \\narena game called \\u2018Dota 2\\u2019. Despite operating independently, these agents learned to work as a cohesive \\nteam to coordinate strategies within the game.\",\"The early years of OpenAI were marked with rapid experimentation. The company made significant progress \\non research in deep learning and reinforcement learning, and released \\u2018OpenAI Gym\\u2019 in 2016, a toolkit \\nfor developing and comparing reinforcement learning algorithms.\",\"OpenAI was initially founded in 2015 by Sam Altman, Elon Musk, Ilya Sutskever and Greg Brockman as a \\nnon-profit organization with the stated goal to \\u201cadvance digital intelligence in the way that is most \\nlikely to benefit humanity as a whole.\\u201d The company assembled a team of the best researchers in the \\nfield of AI to pursue the goal of building AGI in a safe way.\"]},\"ground_truths\":{\"0\":[\"OpenAI Five\"],\"1\":[\"2015\"],\"2\":[\"To advance digital intelligence in a way that benefits humanity\"],\"3\":[\"OpenAI Gym\"],\"4\":[\"Dota 2\"]},\"context_precision\":{\"0\":1.0,\"1\":0.5,\"2\":0.9999999999,\"3\":0.9999999999,\"4\":0.9999999999},\"context_recall\":{\"0\":1.0,\"1\":1.0,\"2\":1.0,\"3\":1.0,\"4\":1.0},\"faithfulness\":{\"0\":1.0,\"1\":1.0,\"2\":1.0,\"3\":1.0,\"4\":1.0},\"answer_relevancy\":{\"0\":1.0,\"1\":1.0,\"2\":1.0,\"3\":0.9253182918,\"4\":1.0}}"
  const obj = JSON.parse(text);
  let length = 0
  let columns = 0
  let values = []

  if (data === null){
    setData(obj)
  }
  if (data){

    columns = Object.keys(data);
    length = Object.keys(data[columns[0]]).length;

    for(let j=0; j < length; j ++){
      let row_values = []
      for (let i in columns){
        let column_name = columns[i]
        console.log("column name: ", column_name, "data: ", data[column_name][j])
      }
    }
  }

  // useEffect(() => {
  //   const fetchData = async () => {
  //     try {
  //       const response = await axios.post('http://127.0.0.1:5000/api/v1/chat', { question: 'your-question' });
  //       setData(response.data.data); // Assuming the 'data' property contains the DataFrame JSON
  //     } catch (error) {
  //       console.error('Error fetching data:', error);
  //     }
  //   };

  //   fetchData();
  // }, []);

  if (!data) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Data Visualization</h2>
      <table>
        <thead>
          <tr>
            {Object.keys(data).map((key) => (
              <th key={key}>{key}</th>
            ))}
          </tr>
        </thead>
        <tbody>
        

          // data.map((row, index) => (
          //   <tr key={index}>
          //     {Object.values(row).map((value, subIndex) => (
          //       <td key={subIndex}>{value}</td>
          //     ))}
          //   </tr>
          // ))
          }
        </tbody>
      </table>
    </div>
  );
};

export default YourComponent;
