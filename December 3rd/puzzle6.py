from matrix import Matrix


def generateClaimsFile():
    claim_details = {}
    with open("input.txt") as claims:
        for claim in claims:
            claim = claim[:-1].split(" @ ")
            cid = int(claim[0][1:])
            claim = claim[1].split(": ")
            dist_from_left, dist_from_top = int(claim[0].split(",")[0]), int(claim[0].split(",")[1])
            width, height = int(claim[1].split("x")[0]), int(claim[1].split("x")[1])
            claim_details[cid] = [dist_from_left, dist_from_top, width, height]
    return claim_details


def findUniqueClaims(parent_matrix, claims_file):
    complete_cid_set = set()
    for cid in claims_file:
        complete_cid_set.add(cid)
        dist_from_left = claims_file[cid][0]
        dist_from_top = claims_file[cid][1]
        width = claims_file[cid][2]
        height = claims_file[cid][3]
        parent_matrix.fillSubMatrixByClaimId(cid, dist_from_left, dist_from_top, width, height)
    common_cids = parent_matrix.findCommonClaims()
    print("ID(s) of the unique claim:", complete_cid_set - common_cids)


if __name__ == '__main__':
    claims_file = generateClaimsFile()
    fabric = Matrix(1000, 1000)
    findUniqueClaims(fabric, claims_file)
