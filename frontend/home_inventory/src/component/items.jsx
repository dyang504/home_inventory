import React from "react";
import { useStoreState } from "easy-peasy";
import { Route, Switch, Link } from "react-router-dom";
import ItemDetail from "./itemDetail";

function Items() {
  const items = useStoreState((state) => state.items);

  return (
    <div>
      <h2>My Items </h2>{" "}
      {items.map((item, key) => (
        <p key={key}>
          <Link
            to={{
              pathname: `/item/${key}`,
              state: {
                itemDetail: item,
              },
            }}
          >
            {item.name}
          </Link>
        </p>
      ))}
    </div>
  );
}

export default Items;
