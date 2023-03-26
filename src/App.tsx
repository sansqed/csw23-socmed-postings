import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';
import Topbar from './Components/Topbar/Topbar';
import Card from './Components/Card/Card';
import Papa, { ParseResult } from 'papaparse';
import data from "./posts.json"

function App() {

  // console.log(data)

  return (
    <div className='App'>
      <Topbar
        hashtag={"#komsaiweek2023"}
      />
      <div className='grid-container'>
        {data.length && data? data.map(({id, author, author_img, date_time, text, imgs})=>{
          return(<Card
            author={author}
            author_img={author_img}
            date_time={date_time}
            text={text}
            imgs={imgs}
            key={id}
          />)
        }):<></>}
      </div>
    </div>
  );
}

export default App;
