def paper_needed(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

def ribbon_needed(l, w, h):
    return 2 * sum(sorted([l, w, h])[:2]) + l*w*h

total_paper_needed = 0
total_ribbon_needed = 0

with open('input', 'r') as f:
    for line in f:
        dim_list = [int(dim) for dim in line.strip().split('x')]
        total_paper_needed += paper_needed(*dim_list)
        total_ribbon_needed += ribbon_needed(*dim_list)

print total_paper_needed
print total_ribbon_needed
