import './App.css';
// import axios from 'axios';

const App = () => {

  const goSearch = (event) => {
    
    const searchInputValue = event.target.elements["search-data"].value;

    // 이제 searchInputValue를 사용하여 검색 또는 필요한 작업을 수행할 수 있음

    console.log("검색어:", searchInputValue);
  };

  return (
    <div className="screen">
      <div className="header">
        <div>
          <form onSubmit={goSearch} className="search-area">
            <input className="search-input" type="text" id='search-data' placeholder='종목을 검색하세요'></input>
            <button className="search-button" type='submit'> 검색 </button>
          </form>
        </div>
      </div>
      <div className='body'>
        <div className="menu">
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
