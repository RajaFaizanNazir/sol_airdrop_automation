import os

address = ['3KhxBQXLnX3Z7xXw4eCBB8ktgf5Wmh2tqxv2pPxjPeFo', 'AT1VNvv9Qq6FsKDE2Kw4TekPyBm99FsHat67UCnNLKdo',
           'vo5K5nRWXiKHZioP4tsbd7vYYTr1azv5YDdiSoiVSFd', '5AL4syXtyjjTNmVyYewUS6dSs3NsJEBArERTBpRFuuBt',
           '6Xm72PN8Rwou5YgaEGuBTPAE5KTadNqwjHtATAfbu6vP', '7hh5a1L6L1L5e4qvys7BsxVcWb9iVyo1KuZAsC6NJgyZ']
for addr in address:
    for i in range(12):
        os.system(('solana airdrop 2 ' + addr))
