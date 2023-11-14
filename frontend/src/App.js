import './App.css';
import React, {useState} from 'react';
import axios from 'axios';

const App = () => {
  const [data, setData] = useState(null);
  const [inputValue, setInputValue] = useState('');
  const [inputStartDate, setStartDate] = useState('');
  const [inputEndDate, setEndDate] = useState('');

  const onClick = () => {
    axios.get(`http://localhost:8000/search/${inputValue}&${inputStartDate}&${inputEndDate}`)
      .then(response => {
        console.log(response.data);
        console.log(response.data.data);
        setData(response.data.data);
      })
      .catch(error => {
        console.error('데이터를 불러오는 중 오류 발생:', error);
      });
  }

  const handleInputChange = (e) => {
    // 사용자가 입력할 때 마다 inputValue 상태를 업데이트
    console.log(e.target.value)
    setInputValue(e.target.value);
  }

  const handleStartDateChange = (e) => {
    console.log(e.target.value)
    setStartDate(e.target.value);
  }

  const handleEndDateChange = (e) => {
    console.log(e.target.value)
    setEndDate(e.target.value);
  }

  return (
    <div className="screen">
      <div className="header">
        <div>
          <form className="search-area">
            <input className="search-input" type="text" id='search-data' placeholder='종목을 검색하세요'
               value={inputValue} onChange={handleInputChange}></input>

            <label>시작일
            <input className="date-input" type="date" id="date-date"
              value={inputStartDate} onChange={handleStartDateChange}></input>
            </label>

            <label>종료일
            <input className="date-input" type="date" id="date-date"
              value={inputEndDate} onChange={handleEndDateChange}></input>
            </label>
            
            <button type="button" className="search-button" onClick={onClick}> 검색 </button>
          </form>
        </div>
      </div>
      <div className='body'>
        <div className="menu">
          {data && data.map((item, index) => (
            <div key={index}>
              {item.company_name} {item.item}
            </div>
          ))}
        </div>
        <div className='body-title'>
        </div>
        <div className='background-block'>
          <div className="body-top-block">
          <div className='body-block' id="top-block"></div>
          <div className='body-block' id="top-block"></div>
          <div className='body-block' id="top-block"></div>
          </div>
          <div className="body-bottom-block">
          <div className='left-side-block'></div>
          <div className='body-block' id='main-block'></div>
          <div className='right-side-block'></div>
        </div>
      </div>
      </div>
    </div>
  );
}

export default App;
