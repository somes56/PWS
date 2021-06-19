---mst_Term
INSERT INTO public."mst_Term"("ID", "Name", "Type", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "IsActive")
VALUES(uuid_generate_v4(),'C.O.D',0,current_timestamp,NULL,current_timestamp,NULL,true);
INSERT INTO public."mst_Term"("ID", "Name", "Type", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "IsActive")
VALUES(uuid_generate_v4(),'CASH',1,current_timestamp,NULL,current_timestamp,NULL,true);
INSERT INTO public."mst_Term"("ID", "Name", "Type", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "IsActive")
VALUES(uuid_generate_v4(),'NET 14TH AFTER EOM',14,current_timestamp,NULL,current_timestamp,NULL,true);
INSERT INTO public."mst_Term"("ID", "Name", "Type", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "IsActive")
VALUES(uuid_generate_v4(),'NET 30TH AFTER EOM',30,current_timestamp,NULL,current_timestamp,NULL,true);
INSERT INTO public."mst_Term"("ID", "Name", "Type", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "IsActive")
VALUES(uuid_generate_v4(),'NET 60TH AFTER EOM',60,current_timestamp,NULL,current_timestamp,NULL,true);
INSERT INTO public."mst_Term"("ID", "Name", "Type", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "IsActive")
VALUES(uuid_generate_v4(),'NET 90TH AFTER EOM',90,current_timestamp,NULL,current_timestamp,NULL,true);

---mst_State
INSERT INTO public."mst_State"("ID", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(),'PERLIS',true,current_timestamp,NULL,current_timestamp,NULL);
INSERT INTO public."mst_State"("ID", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(),'KEDAH',true,current_timestamp,NULL,current_timestamp,NULL);
INSERT INTO public."mst_State"("ID", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(),'PENANG',true,current_timestamp,NULL,current_timestamp,NULL);
INSERT INTO public."mst_State"("ID", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(),'PERAK',true,current_timestamp,NULL,current_timestamp,NULL);
INSERT INTO public."mst_State"("ID", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(),'SELANGOR',true,current_timestamp,NULL,current_timestamp,NULL);
INSERT INTO public."mst_State"("ID", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(),'PUTRAJAYA',true,current_timestamp,NULL,current_timestamp,NULL);
INSERT INTO public."mst_State"("ID", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(),'KUALA LUMPUR',true,current_timestamp,NULL,current_timestamp,NULL);
INSERT INTO public."mst_State"("ID", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(),'NEGERI SEMBILAN',true,current_timestamp,NULL,current_timestamp,NULL);
INSERT INTO public."mst_State"("ID", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(),'MELAKA',true,current_timestamp,NULL,current_timestamp,NULL);
INSERT INTO public."mst_State"("ID", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(),'JOHOR',true,current_timestamp,NULL,current_timestamp,NULL);
INSERT INTO public."mst_State"("ID", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(),'PAHANG',true,current_timestamp,NULL,current_timestamp,NULL);
INSERT INTO public."mst_State"("ID", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(),'KELANTAN',true,current_timestamp,NULL,current_timestamp,NULL);
INSERT INTO public."mst_State"("ID", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(),'TERENGGANU',true,current_timestamp,NULL,current_timestamp,NULL);
INSERT INTO public."mst_State"("ID", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(),'SABAH',true,current_timestamp,NULL,current_timestamp,NULL);
INSERT INTO public."mst_State"("ID", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(),'SARAWAK',true,current_timestamp,NULL,current_timestamp,NULL);
INSERT INTO public."mst_State"("ID", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(),'LABUAN',true,current_timestamp,NULL,current_timestamp,NULL);
INSERT INTO public."mst_State"("ID", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(),'OTHERS',true,current_timestamp,NULL,current_timestamp,NULL);

--sys_Company
INSERT INTO "sys_Company" ("ID", "Code", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(), 'HQ','PIONEERPAC SDN BHD (HQ)', TRUE, current_timestamp, NULL, current_timestamp, NULL);
INSERT INTO "sys_Company" ("ID", "Code", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(), 'WP','PIONEERPAC SDN BHD (WP)', TRUE, current_timestamp, NULL, current_timestamp, NULL);
INSERT INTO "sys_Company" ("ID", "Code", "Name", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy")
VALUES(uuid_generate_v4(), 'NP','PIONEERPAC SDN BHD (NP)', TRUE, current_timestamp, NULL, current_timestamp, NULL);

--mst_DefaultItem
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'ND3Q1', 20.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '36c859fc-7cc4-4a9e-9c3d-3c1a6ef2d5de');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'ND3Q1', 2.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, 'e60d4a06-139f-4a25-a78d-b631ff58a88a');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'ND3Q2', 12.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '36c859fc-7cc4-4a9e-9c3d-3c1a6ef2d5de');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'ND3Q2', 2.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, 'e60d4a06-139f-4a25-a78d-b631ff58a88a');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'ND4Q1', 20.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '36c859fc-7cc4-4a9e-9c3d-3c1a6ef2d5de');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'ND4Q1', 2.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, 'e60d4a06-139f-4a25-a78d-b631ff58a88a');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'ND4Q1', 4.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, '7fd63b7a-70dc-4f21-ac74-a1149ba59222');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'ND4Q1', 3.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '60fc1ef9-d661-4e15-8ec5-dcc01cf7d05e');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'ND4Q2', 12.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '36c859fc-7cc4-4a9e-9c3d-3c1a6ef2d5de');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'ND4Q2', 2.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, 'e60d4a06-139f-4a25-a78d-b631ff58a88a');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'ND4Q2', 4.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, '7fd63b7a-70dc-4f21-ac74-a1149ba59222');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'ND4Q2', 3.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '60fc1ef9-d661-4e15-8ec5-dcc01cf7d05e');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'DD3Q1', 20.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '36c859fc-7cc4-4a9e-9c3d-3c1a6ef2d5de');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'DD3Q1', 2.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, 'e60d4a06-139f-4a25-a78d-b631ff58a88a');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'DD3Q2', 12.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '36c859fc-7cc4-4a9e-9c3d-3c1a6ef2d5de');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'DD3Q2', 2.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, 'e60d4a06-139f-4a25-a78d-b631ff58a88a');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'DD4Q1', 20.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '36c859fc-7cc4-4a9e-9c3d-3c1a6ef2d5de');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'DD4Q1', 2.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, 'e60d4a06-139f-4a25-a78d-b631ff58a88a');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'DD4Q2', 12.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '36c859fc-7cc4-4a9e-9c3d-3c1a6ef2d5de');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'IN', 'DD4Q2', 2.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, 'e60d4a06-139f-4a25-a78d-b631ff58a88a');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'ND3Q1', 20.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '36c859fc-7cc4-4a9e-9c3d-3c1a6ef2d5de');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'DD3Q1', 20.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '36c859fc-7cc4-4a9e-9c3d-3c1a6ef2d5de');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'ND3Q2', 12.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '36c859fc-7cc4-4a9e-9c3d-3c1a6ef2d5de');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'DD3Q2', 12.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '36c859fc-7cc4-4a9e-9c3d-3c1a6ef2d5de');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'ND4Q1', 20.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '36c859fc-7cc4-4a9e-9c3d-3c1a6ef2d5de');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'DD4Q1', 20.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '36c859fc-7cc4-4a9e-9c3d-3c1a6ef2d5de');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'ND4Q2', 12.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '36c859fc-7cc4-4a9e-9c3d-3c1a6ef2d5de');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'DD4Q2', 12.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '36c859fc-7cc4-4a9e-9c3d-3c1a6ef2d5de');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'ND3Q1', 0.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '7fd63b7a-70dc-4f21-ac74-a1149ba59222');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'DD3Q1', 0.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '7fd63b7a-70dc-4f21-ac74-a1149ba59222');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'ND3Q2', 0.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '7fd63b7a-70dc-4f21-ac74-a1149ba59222');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'DD3Q2', 0.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '7fd63b7a-70dc-4f21-ac74-a1149ba59222');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'ND4Q1', 4.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, '7fd63b7a-70dc-4f21-ac74-a1149ba59222');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'DD4Q1', 0.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '7fd63b7a-70dc-4f21-ac74-a1149ba59222');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'ND4Q2', 4.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, '7fd63b7a-70dc-4f21-ac74-a1149ba59222');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'DD4Q2', 0.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '7fd63b7a-70dc-4f21-ac74-a1149ba59222');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'ND3Q1', 0.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '60fc1ef9-d661-4e15-8ec5-dcc01cf7d05e');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'DD3Q1', 0.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '60fc1ef9-d661-4e15-8ec5-dcc01cf7d05e');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'ND3Q2', 3.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '60fc1ef9-d661-4e15-8ec5-dcc01cf7d05e');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'DD3Q2', 0.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '60fc1ef9-d661-4e15-8ec5-dcc01cf7d05e');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'ND4Q1', 3.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '60fc1ef9-d661-4e15-8ec5-dcc01cf7d05e');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'DD4Q1', 0.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '60fc1ef9-d661-4e15-8ec5-dcc01cf7d05e');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'ND4Q2', 3.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '60fc1ef9-d661-4e15-8ec5-dcc01cf7d05e');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'DD4Q2', 0.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, '60fc1ef9-d661-4e15-8ec5-dcc01cf7d05e');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'ND3Q1', 2.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, 'e60d4a06-139f-4a25-a78d-b631ff58a88a');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'DD3Q1', 2.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, 'e60d4a06-139f-4a25-a78d-b631ff58a88a');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'ND3Q2', 0.00, TRUE, current_timestamp, NULL, current_timestamp, NULL, 'e60d4a06-139f-4a25-a78d-b631ff58a88a');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'DD3Q2', 2.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, 'e60d4a06-139f-4a25-a78d-b631ff58a88a');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'ND4Q1', 2.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, 'e60d4a06-139f-4a25-a78d-b631ff58a88a');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'DD4Q1', 2.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, 'e60d4a06-139f-4a25-a78d-b631ff58a88a');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'ND4Q2', 2.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, 'e60d4a06-139f-4a25-a78d-b631ff58a88a');
INSERT INTO public."mst_DefaultItem"("ID", "AccountType", "Code", "Amount", "IsActive", "CreateDate", "CreateBy", "UpdateDate", "UpdateBy", "ItemID")
VALUES(uuid_generate_v4(), 'CN', 'DD4Q2', 2.50, TRUE, current_timestamp, NULL, current_timestamp, NULL, 'e60d4a06-139f-4a25-a78d-b631ff58a88a');