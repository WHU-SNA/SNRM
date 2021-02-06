numNodes = size(positive_SAFT);
numNodes = numNodes(1);
k = 32;

for i = 1: numNodes
    positive_SAFT(isnan(positive_SAFT(:, i)), i) = max(positive_SAFT(:, i));
end
sht = -log(positive_SAFT);
[U, S, V] = svds(sht, k);
out_emb_1 = U * (S ^ (1/2));
in_emb_1 = V * (S ^ (1/2));

for i = 1: numNodes
    negative_SAFT(isnan(negative_SAFT(:, i)), i) = max(negative_SAFT(:, i));
end
sht = log(negative_SAFT);
[U, S, V] = svds(sht, k);
out_emb_2 = U * (S ^ (1/2));
in_emb_2 = V * (S ^ (1/2));

for i = 1: numNodes
    positive_SAFT(i, i) = 1;
    negative_SAFT(i, i) = 1;
end
sht = log(negative_SAFT ./ positive_SAFT);
[U, S, V] = svds(sht, k);
out_emb_3 = U * (S ^ (1/2));
in_emb_3 = V * (S ^ (1/2));
