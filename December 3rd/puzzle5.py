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


def overlapsInFabric(parent_matrix, claims_file):
    for cid in claims_file:
        dist_from_left = claims_file[cid][0]
        dist_from_top = claims_file[cid][1]
        width = claims_file[cid][2]
        height = claims_file[cid][3]
        parent_matrix.fillSubMatrix(dist_from_left, dist_from_top, width, height)
    print("Sq. inches of fabric covered by 2 or more claims =", parent_matrix.findOverlapsInMatrix())


if __name__ == '__main__':
    claims_file = generateClaimsFile()
    fabric = Matrix(1000, 1000)
    overlapsInFabric(fabric, claims_file)
