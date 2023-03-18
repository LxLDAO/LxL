require('dotenv').config();

const Web3 = require('web3');
import { ethers } from "hardhat";
import { Signer } from "ethers";

async function deployContract(name: any, args: any) {
  const factory = await ethers.getContractFactory(name);
  return await factory.deploy(...args)
}


describe("LxL Test", function() {
    before(async function() {
        this.signers = await ethers.getSigners();
        this.deployer = this.signers[0];
        
        this.LxL = await deployContract("LxL",[]);
    })

    it("mint NFT", async function() {
        await this.LxL.mint("ipfs://QmU6YFSdk6gqSAiect9QDQUtmDv9SHm6cqxJLRn9a7u7YU")
    })
})
