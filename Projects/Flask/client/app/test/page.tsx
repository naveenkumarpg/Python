'use client';
import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Members() {
  const [data, setData] = useState('');
  useEffect(() => {
    const fetchData = () => {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/',
        data: {
          firstName: 'Fred',
          lastName: 'Flintstone',
        },
      })
        .then((response) => {
          setData(response.data);
        })
        .catch((error) => {
          console.error('There was an error!', error);
        });
    };

    fetchData();
  }, []);

  return <div>{data && JSON.stringify(data)}</div>;
}

export default Members;
