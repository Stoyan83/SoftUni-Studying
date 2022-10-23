function manage(arr, str) {
  class Ticket {
    constructor(destination, price, status) {
      this.destination = destination;
      this.price = price;
      this.status = status;
    }
  }
  let tickets = [];

  for (const ticket of arr) {
    let [destination, price, status] = ticket.split("|");
    tickets.push(new Ticket(destination, Number(price), status));
  }

  tickets.sort((a, b) => str === "price" ? a[str] - b[str] : a[str].localeCompare(b[str])
  );

  return tickets;
}

console.log(
  manage(
    [
      "Philadelphia|94.20|available",
      "New York City|95.99|available",
      "New York City|95.99|sold",
      "Boston|126.20|departed",
    ],
    "destination"
  )
);

manage(
  [
    "Philadelphia|94.20|available",
    "New York City|95.99|available",
    "New York City|95.99|sold",
    "Boston|126.20|departed",
  ],
  "status"
);
