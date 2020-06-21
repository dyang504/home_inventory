import React, { useEffect, useState } from "react";
import { useStoreState } from "easy-peasy";

import { BrowserRouter as Router, useParams } from "react-router-dom";

function ItemDetail() {
  let { key } = useParams();
  // const [isLoad, setIsLoad] = useState(false);
  // const [itemDetail, setItemDetail] = useState({});
  let itemDetail = useStoreState((state) => state.items[key]);

  // useEffect(() => {
  //   let headers = { "Content-Type": "application.json" };
  //   headers["Authorization"] =
  //     "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ5YW5nIiwiZXhwIjoxNTkyNzI1MjA0fQ._OuV9zfO6Q9R04DtuRg9mCa_opZRrlwkWTB6ANZZmkc";
  //   fetch("http://127.0.0.1:8000/itemlist", { headers })
  //     .then((res) => res.json())
  //     .then((result) => {
  //       setItemDetail(result[2]);
  //       setIsLoad(true);
  //     });
  // });
  // if (!isLoad) {
  // return <div>Loading...</div>;
  // } else {
  return (
    <div>
      <h3>Name: {itemDetail.name}</h3>
      <h3>Category</h3>
      <p>{itemDetail.category[0].name}</p>
      <h3>Infomation</h3>
      <p>Price: {itemDetail.infos[0].price}</p>
      <p>Expiration date: {itemDetail.infos[0].expiration_date}</p>
      <p>Purchase date: {itemDetail.infos[0].purchase_date}</p>
      <h3>Nutritions</h3>
      <p>
        {itemDetail.nutritions[0].name} {itemDetail.nutritions[0].value} g{" "}
        {itemDetail.nutritions[0].unit}
      </p>
      <h3>Images</h3>
      <h3>Size</h3>
      <p>
        {/*         
{itemDetail.size[0].indicator_name}: {itemDetail.size[0].value}
{itemDetail.size[0].unit} */}
      </p>
      <p></p>
    </div>
  );
  // }
}

export default ItemDetail;
