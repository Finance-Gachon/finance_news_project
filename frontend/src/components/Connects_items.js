import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Connnects_items() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        // 요청이 시작 할 때에는 error 와 result 를 초기화하고
        setError(null);
        setResult(null);
        // loading 상태를 true 로 바꿉니다.
        setLoading(true);
        const response = await axios.get(
          'http://localhost:8000/items/13?q=hungry'
        );
        setResult(response.data); // 데이터는 response.data 안에 들어있습니다.
      } catch (e) {
        setError(e);
      }
      setLoading(false);
    };

    fetchUsers();
  }, []);

  if (loading) return <div>로딩중..</div>;
  if (error) return <div>에러가 발생했습니다</div>;
  if (!result) return null;
  return (
    <div>
      {result.item_id}
      <br></br>
      {result.q}
    </div>
  );
}

export default Connnects_items;