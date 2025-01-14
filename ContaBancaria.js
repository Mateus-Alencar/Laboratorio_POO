// Classe base: Conta Bancária
class ContaBancaria {
    constructor(cliente, numeroConta, saldoInicial) {
      this.cliente = cliente;
      this.numeroConta = numeroConta;
      this._saldo = saldoInicial; // Propriedade privada simulada
    }
  
    // Método para verificar o saldo
    verificarSaldo() {
      console.log(`Saldo atual de ${this.cliente}: R$ ${this._saldo.toFixed(2)}`);
    }
  
    // Método para depositar
    depositar(valor) {
      if (valor > 0) {
        this._saldo += valor;
        console.log(`Depósito de R$ ${valor.toFixed(2)} realizado com sucesso.`);
      } else {
        console.log("O valor do depósito deve ser positivo.");
      }
    }
  
    // Método para sacar
    sacar(valor) {
      if (valor > 0 && valor <= this._saldo) {
        this._saldo -= valor;
        console.log(`Saque de R$ ${valor.toFixed(2)} realizado com sucesso.`);
      } else {
        console.log("Saldo insuficiente ou valor inválido.");
      }
    }
  }
  
  // Classe derivada: Conta Poupança
  class ContaPoupanca extends ContaBancaria {
    constructor(cliente, numeroConta, saldoInicial, taxaJuros) {
      super(cliente, numeroConta, saldoInicial); // Chamada ao construtor da classe base
      this.taxaJuros = taxaJuros;
    }
  
    // Método para aplicar juros
    aplicarJuros() {
      const juros = this._saldo * (this.taxaJuros / 100);
      this._saldo += juros;
      console.log(`Juros de R$ ${juros.toFixed(2)} aplicados.`);
    }
  }
  
  // Classe derivada: Conta Corrente
  class ContaCorrente extends ContaBancaria {
    constructor(cliente, numeroConta, saldoInicial, limiteChequeEspecial) {
      super(cliente, numeroConta, saldoInicial);
      this.limiteChequeEspecial = limiteChequeEspecial;
    }
  
    // Sobrescrevendo o método sacar para incluir cheque especial
    sacar(valor) {
      if (valor > 0 && valor <= this._saldo + this.limiteChequeEspecial) {
        this._saldo -= valor;
        console.log(`Saque de R$ ${valor.toFixed(2)} realizado com sucesso.`);
      } else {
        console.log("Saldo insuficiente, mesmo considerando o limite.");
      }
    }
  }
  
  // Teste do sistema bancário
  const contaPoupanca = new ContaPoupanca("João", 12345, 1000, 1.5);
  contaPoupanca.verificarSaldo();
  contaPoupanca.depositar(500);
  contaPoupanca.aplicarJuros();
  contaPoupanca.verificarSaldo();
  
  console.log("-----------------");
  
  const contaCorrente = new ContaCorrente("Maria", 67890, 500, 1000);
  contaCorrente.verificarSaldo();
  contaCorrente.sacar(800);
  contaCorrente.verificarSaldo();
  contaCorrente.sacar(1000); // Tentativa de ultrapassar o limite
  