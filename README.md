# Fyle

## Endpoints

* fyle-in.herokuapp.com/ifsc/ : Provides the details of the branch.

Expects `ifsc` of the branch
```
{
  "ifsc":"ABHY0065001"
}
```
* fyle-in.herokuapp.com/branch_list/ : Provides detailed list of all the branches given the name of the bank and city.

Expects `name` of the bank and `city`.
```
{
  "city":"MUMBAI",
  "name":"ABHYUDAYA COOPERATIVE BANK LIMITED"
}
```


To access `admin` click <a href="https://fyle-in.herokuapp.com/admin">here</a>
