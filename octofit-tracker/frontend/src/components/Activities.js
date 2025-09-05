import React, { useEffect, useState } from 'react';

const apiUrl = () => {
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  return codespace
    ? `https://${codespace}-8000.app.github.dev/api/activities/`
    : 'http://localhost:8000/api/activities/';
};

function Activities() {
  const [data, setData] = useState([]);
  useEffect(() => {
    const url = apiUrl();
    console.log('Fetching Activities from:', url);
    fetch(url)
      .then(res => res.json())
      .then(json => {
        const results = json.results || json;
        setData(results);
        console.log('Activities data:', results);
      });
  }, []);
  return (
    <div className="container">
      <h2 className="my-4 display-6">Activities</h2>
      <table className="table table-striped table-bordered">
        <thead className="table-light">
          <tr>
            <th>Type</th>
            <th>Duration (min)</th>
            <th>Calories</th>
          </tr>
        </thead>
        <tbody>
          {data.map((item, idx) => (
            <tr key={item._id || idx}>
              <td>{item.type}</td>
              <td>{item.duration}</td>
              <td>{item.calories}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
export default Activities;
