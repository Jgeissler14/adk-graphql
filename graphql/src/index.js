const { ApolloServer, gql } = require('apollo-server');
const db = require('./db');

const typeDefs = gql`
  type Customer {
    id: ID!
    name: String!
    email: String!
    phone: String
  }

  type Product {
    id: ID!
    name: String!
    description: String
    price: Float!
  }

  type SalesRecord {
    id: ID!
    customerId: Int!
    productId: Int!
    quantity: Int!
    saleDate: String!
  }

  type Query {
    customers: [Customer!]!
    products: [Product!]!
    salesRecords: [SalesRecord!]!
  }
`;

const resolvers = {
  Query: {
    customers: async () => {
      const { rows } = await db.query(
        'SELECT id, name, email, phone FROM customers'
      );
      return rows;
    },
    products: async () => {
      const { rows } = await db.query(
        'SELECT id, name, description, price FROM products'
      );
      return rows;
    },
    salesRecords: async () => {
      const { rows } = await db.query(
        `SELECT id, customer_id AS "customerId", product_id AS "productId", quantity, sale_date AS "saleDate" FROM sales_records`
      );
      return rows;
    },
  }
};

async function startServer() {
  const server = new ApolloServer({ typeDefs, resolvers });
  const { url } = await server.listen();
  console.log(`Server ready at ${url}`);
}

startServer();
