import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import styled from 'styled-components'; //npm install styled-components


const App = () => {

  const [data, setData] = useState(null);
  const [inputValue, setInputValue] = useState('');
  const [inputStartDate, setStartDate] = useState('');
  const [inputEndDate, setEndDate] = useState('');
  const [valuePN, setValuePN] = useState();
  const [imgPN, setImgPN] = useState();


  const testPN = 0.9  //긍부정 테스트 값
  useEffect(() => {
    if (testPN >= 0.5) {
      setImgPN(<Img src="https://cdn-icons-png.flaticon.com/128/8279/8279617.png" />)
      setValuePN(<H3 style={{ color: "#4a29cf" }}>긍정</H3>)
    }
    else if (testPN <= 0.5) {
      setImgPN(<Img src="https://cdn-icons-png.flaticon.com/128/8279/8279616.png" />)
      setValuePN(<H3 style={{ color: "#cf294a" }}>부정</H3>)
    }

  }, [testPN])




  const TopBlock = styled.div`
  display:flex;
  flex-direction: column;
  background-color: white;
  border-radius: 3vh;
  margin-left: 3vh;
  width: 49vh;
  height: 15vh;`

  const H3 = styled.h3`
  margin-left: 10px;
  margin-bottom: 0;
  width: 40vh;
  font-weight: bold;
`

  const Img = styled.img`
  margin-left: 30px;
  width:40px;
  `

  const BlockTitle = styled.div`
  margin-top: 15px;
  display:flex;
  flex-direction: row;
  align-content: center;
  justify-content: center;
  width:100%
  `
  const LinkBox = styled.div`
  display:flex;
  flex-direction: column;
  margin-left:50px;
  margin-top:10px;
  `
  const NewsLink = styled.a`
  font-size: 20px
  `
  const RatioBoxPN = styled.div`
  display:flex;
  flex-direction: column;
  align-content: center;
  justify-content: center;
  height: 170px;
  width:100%
  `
  const RatioPN = styled.div`
  display:flex;
  flex-direction: column;
  align-content: center;
  justify-content: center;
  height: 170px;
  width:100%
  `

  const onClick = () => {
    console.log(inputValue)
    // axios.get(`http://localhost:8000/search/${inputValue}&${inputStartDate}&${inputEndDate}`)
    //   .then(response => {
    //     console.log(response.data);
    //     console.log(response.data.data);
    //     setData(response.data.data);
    //   })
    //   .catch(error => {
    //     console.error('데이터를 불러오는 중 오류 발생:', error);
    //   });
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
        <div className='head-area'>
          <form className="search-area" style={{ height: "200px" }}>
            <div className="search-input-area">
              <input className="form-control" style={{ width: "500px", height: "70px", marginBottom: "10px", border: "1px solid #000" }} type="text" id='search-data' placeholder='종목을 검색하세요'
                value={inputValue} onChange={handleInputChange}></input>
              <div className='date-area'>
                <label>시작일
                  <input className="date-input" style={{ borderRadius: "5px", border: "1px solid #000", width: "190px", height: "30px", marginBottom: "10px", marginLeft: "10px", marginRight: "10px" }} type="date" id="date-date"
                    value={inputStartDate} onChange={handleStartDateChange}></input>
                </label>
                <label>종료일
                  <input className="date-input" style={{ borderRadius: "5px", border: "1px solid #000", width: "190px", height: "30px", marginBottom: "10px", marginLeft: "10px" }} type="date" id="date-date"
                    value={inputEndDate} onChange={handleEndDateChange}></input>
                </label>
              </div>
              </div>
            <button type="button" style={{ height: "120px", width: "100px", marginLeft: "20px" }} className="btn btn-outline-primary" onClick={onClick}> 검색 </button>
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

            <TopBlock>
              <BlockTitle>
                <Img src="https://cdn-icons-png.flaticon.com/128/5425/5425638.png" />
                <H3 style={{ color: "#ffc905" }}>최신 뉴스 모음</H3>
              </BlockTitle>
              <LinkBox>
                <NewsLink>test.com</NewsLink>
                <NewsLink>test.com</NewsLink>
                <NewsLink>test.com</NewsLink>
              </LinkBox>
            </TopBlock>
            <TopBlock>
              <BlockTitle>
                {imgPN}
                {valuePN}
              </BlockTitle>
            </TopBlock>
            <TopBlock>
            <RatioBoxPN>
              <RatioPN>

              </RatioPN>
            </RatioBoxPN>
            </TopBlock>
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
