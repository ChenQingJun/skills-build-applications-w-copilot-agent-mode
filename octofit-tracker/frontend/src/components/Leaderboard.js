import React, { useEffect, useState } from 'react';

const apiUrl = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  return codespace
    ? `https://${codespace}-8000.app.github.dev/api/leaderboard/`
    : 'http://localhost:8000/api/leaderboard/';
};

function Leaderboard() {
  const [data, setData] = useState([]);
  useEffect(() => {
    const url = apiUrl();
    console.log('Fetching Leaderboard from:', url);
    fetch(url)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Leaderboard data:', results);
      });
  }, []);
  return (
    <div className="container">
      <h2 className="my-4 display-6">Leaderboard</h2>
      <table className="table table-striped table-bordered">
        <thead className="table-light">
          <tr>
            <th>User</th>
            <th>Score</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, idx) => (
            <tr key={item._id || idx}>
              <td>{item.user?.username || 'Unknown'}</td>
              <td>{item.score}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
export default Leaderboard;
