import { React, useEffect, useState } from "react";
import "./App.css";
import Cards from "./Cards";

const App = () => {
  const [post, setpost] = useState([]);
  const [post2, setpost2] = useState([]);
  useEffect(() => {
    fetch("https://jsonplaceholder.typicode.com/users")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setpost(data);
        setpost2(data);
      })
      .catch((err) => {
        console.log(err.message);
      });
  }, []);


  function checking(pop) {
    if (pop.target.value !== "") {
      let ele = post.filter((ele) => {
        return ele.name.includes(pop.target.value);
      });
      setpost(ele);
    } else {
      setpost(post2);
    }
  }


  return (
    <div className="App">
      <div className="Header-div">
        <h1 className="top-header">Monster Nic</h1>
      </div>
      <div className="search-part2">
        <h5 className="search-part">Enter your Input!</h5>
        <input
          className="input-box"
          type="text"
          placeholder="Enter the name here"
          onChange={checking}
        />
      </div>
      <div className="posts-container mb-3">
        {post.map((post) => {
          return (
            <Cards
              id={post.id}
              name={post.name}
              username={post.username}
              email={post.email}
            />
          );
        })}
      </div>
    </div>
  );
};

export default App;
